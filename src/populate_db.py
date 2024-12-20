from database.db import database
from models.quiz import Question, Option

def populate_db(app):
    with app.app_context():        
        database.create_all()
       
        questions = [
            {
                "question_text": "Bir resim işleme algoritmasında, Kenar Tespiti (Edge Detection) için en yaygın kullanılan yöntemlerden biri aşağıdakilerden hangisidir?",
                "options": [
                    {"option_text": "Gaussian Blur", "is_correct": False},
                    {"option_text": "Sobel Filtresi", "is_correct": True},
                    {"option_text": "Median Filtresi", "is_correct": False},
                    {"option_text": "Histogram Eşitleme", "is_correct": False}
                ]
            },
            {
                "question_text": "Bir görüntüdeki nesneleri tanımlamak ve ayırmak için kullanılan algoritmalardan biri olan “K-means” hangi tür algoritmalar sınıfına aittir?",
                "options": [
                    {"option_text": "Denetimli Öğrenme (Supervised Learning)", "is_correct": False},
                    {"option_text": "Denetimsiz Öğrenme (Unsupervised Learning)", "is_correct": True},
                    {"option_text": "Yarı Denetimli Öğrenme (Semi-Supervised Learning)", "is_correct": False},
                    {"option_text": "Pekiştirmeli Öğrenme (Reinforcement Learning)", "is_correct": False}
                ]
            },
            {
                "question_text": "Bilgisayar görüşünde, bir görüntüdeki belirli özelliklerin yerini belirlemek için kullanılan yöntemlerden biri olan Hough Transformasyonu aşağıdaki problemlerden hangisini çözmek için yaygın olarak kullanılır?",
                "options": [
                    {"option_text": "Renk Dönüşümleri", "is_correct": False},
                    {"option_text": "Gürültü Azaltma", "is_correct": False},
                    {"option_text": "Doğru ve Çember Tespiti", "is_correct": True},
                    {"option_text": "Görüntü Büyütme ve Küçültme", "is_correct": False}
                ]
            }
        ]
       
        for q in questions:
            question = Question(question_text=q["question_text"])
            database.session.add(question)
            database.session.commit()

            for o in q["options"]:
                option = Option(question_id=question.id, option_text=o["option_text"], is_correct=o["is_correct"])
                database.session.add(option)

        database.session.commit()