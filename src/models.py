"""Database Models for application
"""


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



db = SQLAlchemy()


class User(db.Model):
    """
    Represents a User in the system.
    
    Attributes:
        id (int): The primary key of the User.
        username (str): The unique username of the User.
        password (str): The hashed password of the User.
        email (str): The unique email of the User.
        name (str): The name of the User.
        bio (str): The bio of the User.
        created_at (datetime): The date and time the User was created.
        profile_picture (str): Profile picture url
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_picture = db.Column(db.Text, unique=True, nullable=False)
    
    def __str__(self):
        return f"<User(username='{self.username}')>"

    def __repr__(self):
        return self.__str__()



class Story(db.Model):
    """
    Class representing a story.
        Attributes:
            id (int) - The unique id of the story.
            title (str) - The title of the story.
            coverUrl(str) - the link for cover page of story
            author_id (int) - The id of the author of the story.
            genre (str) - The genre of the story.
            summary (str) - A summary of the story.
            content (str) - The content of the story.
            rating (float) - The rating of the story.
            num_ratings (int) - The number of ratings the story has received.
            created_at (datetime) - The date and time when the story was created.
            author (User) - The User object representing the author of the story.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    coverUrl = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    genre = db.Column(db.String(120), nullable=True)
    summary = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    num_ratings = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.relationship("User", backref=db.backref("stories", lazy=True))

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<Story {self.title}>'


class Rating(db.Model):
    """
    Rating class representing the ratings table in the database
    Attributes:
        id (int): Unique identifier for the rating
        story_id (int): Id of the story the rating belongs to
        user_id (int): Id of the user who gave the rating
        rating (int): The rating given by the user
        created_at (datetime): The date and time the rating was created
        story (Story): Relationship to the story the rating belongs to
        user (User): Relationship to the user who gave the rating
    """
    id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    story = db.relationship("Story", backref=db.backref("ratings", lazy=True))
    user = db.relationship("User", backref=db.backref("ratings", lazy=True))

    def __str__(self):
        return f'<Rating {self.id}>'

    def __repr__(self):
        return self.__str__()


class Review(db.Model):
    """
    Review model for storing reviews of stories.

    Attributes:
        id (int): The primary key for the review.
        story_id (int): The foreign key for the story being reviewed.
        user_id (int): The foreign key for the user who wrote the review.
        rating (int): The rating given by the user for the story.
        review_text (str): The text of the review.
        created_at (datetime): The date and time when the review was created.
        story (obj): Relationship with the story being reviewed.
        user (obj): Relationship with the user who wrote the review.
    """
    id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    story = db.relationship("Story", backref=db.backref("reviews", lazy=True))
    user = db.relationship("User", backref=db.backref("reviews", lazy=True))

    def __repr__(self):
        return f'<Review id={self.id} title={self.title}>'

    def __str__(self):
        return f'Review {self.id} - {self.title}'

