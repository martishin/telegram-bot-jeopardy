import re

from ml.model import QuestionAnsweringModel

qa_model = QuestionAnsweringModel()


def check_percent(text):
    """Check if the output contains a percentage similarity above 50%."""
    percent_pat = re.compile(r"(\d{2})(?=%)")
    find_percent = re.search(percent_pat, text)
    assert (
        find_percent is not None
    ), "Your output should contain the similarity rank, but it doesn't."

    percent = int(find_percent.group(0))
    assert (
        percent >= 50
    ), "Similarity rank is too low. Please, check the parameters and retrain your model."


def test_question_1():
    question = """The song "Cherish" was the first No. 1 hit for this L.A. band"""
    question_number, certainty, answer = qa_model.infer_answer(question)

    assert (
        question_number == 76740
    ), "The number of the closest topic is wrong. Please check the parameters and retrain your model."
    check_percent(f"{certainty}%")
    assert "the association" in answer.lower(), "The selected answer is incorrect."


def test_question_2():
    question = "This butterfly-shaped gland straddles the windpipe just behind the Adam's apple"
    question_number, certainty, answer = qa_model.infer_answer(question)

    assert (
        question_number == 76900
    ), "The number of the closest topic is wrong. Please check the parameters and retrain your model."
    check_percent(f"{certainty}%")
    assert "thyroid" in answer.lower(), "The selected answer is incorrect."


def test_question_3():
    question = "In Egypt & Algeria, some areas of this desert are below sea level"
    question_number, certainty, answer = qa_model.infer_answer(question)

    assert (
        question_number == 79995
    ), "The number of the closest topic is wrong. Please check the parameters and retrain your model."
    check_percent(f"{certainty}%")
    assert "sahara" in answer.lower(), "The selected answer is incorrect."


def test_question_4():
    question = "After converting this Balkan country to Christianity, Czar Boris I put out his own son's eyes"
    question_number, certainty, answer = qa_model.infer_answer(question)

    assert (
        question_number == 51508
    ), "The number of the closest topic is wrong. Please check the parameters and retrain your model."
    check_percent(f"{certainty}%")
    assert "bulgaria" in answer.lower(), "The selected answer is incorrect."


def test_question_5():
    question = 'The name of this ballroom dance with gliding turns comes from German for "roll" or "turn"'
    question_number, certainty, answer = qa_model.infer_answer(question)

    assert (
        question_number == 19908
    ), "The number of the closest topic is wrong. Please check the parameters and retrain your model."
    check_percent(f"{certainty}%")
    assert "waltz" in answer.lower(), "The selected answer is incorrect."
