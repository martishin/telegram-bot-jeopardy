import logging
import pathlib

import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess

if not logging.getLogger().hasHandlers():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

logger = logging.getLogger(__name__)

BASE_DIR = pathlib.Path(__file__).parent.resolve()
DATA_NAME = BASE_DIR / "data" / "JEOPARDY_CSV.csv"
MODEL_NAME = BASE_DIR / "data" / "JEOPARDY_CSV.model"

VECTOR_SIZE = 124
EPOCHS = 40


class QuestionAnsweringModel:
    def __init__(self):
        logging.info("Initializing model...")
        self.df = pd.read_csv(DATA_NAME)
        self.question_field = self.df.columns[5]
        self.answer_field = self.df.columns[6]

        self.model = self.load_or_train_model()

    def load_or_train_model(self):
        if not pathlib.Path(MODEL_NAME).is_file():
            logging.info(f"Model not found at {MODEL_NAME}. Training a new model.")
            return self.train_model()
        else:
            logging.info(f"Loading existing model from {MODEL_NAME}.")
            return Doc2Vec.load(str(MODEL_NAME))

    def train_model(self):
        logging.info("Training the model...")
        train_corpus = [
            TaggedDocument(simple_preprocess(question), [number])
            for number, question in enumerate(self.df[self.question_field])
        ]
        model = Doc2Vec(
            vector_size=VECTOR_SIZE, min_count=1, epochs=EPOCHS, hs=1, dbow_words=1
        )
        model.build_vocab(train_corpus)
        model.train(
            train_corpus, total_examples=model.corpus_count, epochs=model.epochs
        )
        model.save(str(MODEL_NAME))
        logging.info(f"Model trained and saved to {MODEL_NAME}.")
        return model

    def infer_answer(self, question):
        logging.info(f"Inferring answer for the question: '{question}'")
        response = self.model.dv.most_similar(
            [self.model.infer_vector(simple_preprocess(question))], topn=1
        )
        question_number = response[0][0]
        certainty = round(response[0][1] * 100)
        answer = self.df.loc[question_number, self.answer_field]
        logging.info(
            f"Answer inferred with {certainty}% certainty: '{answer}' (Question Number: {question_number})"
        )
        return question_number, certainty, answer
