import nltk
food = ["daal", "chawal", "idli", "dosa", "roti"]
movie = ["shimha", "avtar", "RRR", "KGF", "sholay"]

food_paragraph = """I like eating Indian food every day.
My favorite foods are daal, chawal, idli, dosa, and roti. 
Daal and chawal are healthy and simple meals. 
Idli and dosa are popular South Indian foods that many people enjoy for breakfast. 
Roti is commonly eaten with vegetables and curry. 
These foods are tasty, nutritious, and loved by many families in India."""

movie_paragraph = """The movies Shimha, Avatar, RRR, KGF, and Sholay are very popular among audiences. 
RRR and KGF are action-packed films with powerful characters and exciting stories. 
Sholay is a classic Indian movie loved by many generations. 
Avatar is famous for its amazing visual effects and science fiction world. 
People enjoy watching different types of movies for entertainment and relaxation."""

food_text=food_paragraph.lower().split()
movie_text=movie_paragraph.lower().split()

token_food=nltk.word_tokenize(food_text)