from django.db import models

# Create your models here.
# {'response_code': 0, 'results': [{'category': 'Entertainment: Television', 'type': 'multiple', 'difficulty': 'medium', 'question': 'What year did the television company BBC officially launch the channel BBC One?', 'correct_answer': '1936', 'incorrect_answers': ['1948', '1932', '1955']}, {'category': 'Animals', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Kangaroos keep food in their pouches next to their children.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'medium', 'question': 'Which of these is NOT a playable character race in the video game &quot;Starbound&quot;?', 'correct_answer': 'Fenerox', 'incorrect_answers': ['Floran', 'Novakid', 'Hylotl']}, {'category': 'Entertainment: Books', 'type': 'boolean', 'difficulty': 'easy', 'question': '&quot;Elementary, my dear Watson&quot; is a phrase that is never truly said within the Conan Doyle books of Sherlock Holmes.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'Entertainment: Music', 'type': 'multiple', 'difficulty': 'medium', 'question': 'What year was Red Hot Chill Pepper&#039;s album &quot;Californication&quot; released?', 'correct_answer': '1999', 'incorrect_answers': ['1997', '2000', '1992']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In Super Smash Bros. for Nintendo 3DS and Nintendo Wii U, who was the sixth fighter to be added to the game post-launch?', 'correct_answer': 'Corrin', 'incorrect_answers': ['Cloud', 'Bayonnetta', 'Ryu']}, {'category': 'Entertainment: Japanese Anime & Manga', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In &quot;One Piece&quot;, what does &quot;the Pirate King&quot; mean to the captain of the Straw Hat Pirates?', 'correct_answer': 'Freedom', 'incorrect_answers': ['Promise', 'Adventure', 'Friendship']}, {'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'What are Panama hats made out of?', 'correct_answer': 'Straw', 'incorrect_answers': ['Silk', 'Hemp', 'Flax']}, {'category': 'History', 'type': 'multiple', 'difficulty': 'easy', 'question': 'Abolitionist John Brown raided the arsenal in which Virginia Town?', 'correct_answer': 'Harper&#039;s Ferry', 'incorrect_answers': ['Richmond', 'Harrisonburg', 'Martinsburg']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'medium', 'question': 'From where does the Nintendo video game character Mario derive his name?', 'correct_answer': 'The landlord of the American headquarters', 'incorrect_answers': ['Shigeru Miyamoto&#039;s father in law', 'Satoru Iwata&#039;s plumber', 'The date (Mar 10) that Donkey Kong was released.']}]}


class Question(models.Model):
    category = models.CharField(max_length=50)

    question = models.TextField()

    def __str__(self) -> str:
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')

    answer = models.TextField()

    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer
