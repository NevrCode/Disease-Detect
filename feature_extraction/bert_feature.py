
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity




class BertFeature :
    feature = []
    sentence = ''
    def __init__(self, sentence):
        self.stopFactory = StopWordRemoverFactory()
        self.stemFactory = StemmerFactory()
        self.stemmer = self.stemFactory.create_stemmer()
        self.stopwords = self.stopFactory.create_stop_word_remover()  
        self.feature = []
        self.sentence = sentence   
        self.tokenizer = AutoTokenizer.from_pretrained("cahya/bert-base-indonesian-522M")
        self.model = AutoModel.from_pretrained("cahya/bert-base-indonesian-522M")

    def get_sentence_embedding(self, text):
        # Mentokenisasi teks input
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True)
        outputs = self.model(**inputs)

        # Proses Pooling
        embeddings = outputs.last_hidden_state
        sentence_embedding = embeddings.mean(dim=1)

        return sentence_embedding
    
    def get_symptoms(self,text):
  # Topik (gejala penyakit)
        topics = ['demam', 'batuk', 'lemas', 'sesak nafas']

        # Membuat embedding untuk setiap input kata kata dan topik
        sentence_embedding = self.get_sentence_embedding(text)
        topic_embeddings = [self.get_sentence_embedding(topic) for topic in topics]

        # Menghitung kemiripan dengan cosine similarity, dan mengurutkannya
        similarities = [cosine_similarity(sentence_embedding.detach().numpy(), topic_embedding.detach().numpy())[0][0] for topic_embedding in topic_embeddings]
        related_topics = sorted(zip(topics, similarities), key=lambda x: x[1], reverse=True)

        # dictionary untuk output
        data_matrix = {}

        # Output dictionary dengan gejala bersifat boolean
        for topic, score in related_topics:
            score = float(score)
            data_matrix[topic] = score

        return data_matrix

    def get_key_topics(self):
        stemmed = self.stemmer.stem(self.sentence)
        stop_removed = self.stopwords.remove(stemmed)
        return self.get_symptoms(stop_removed)
    