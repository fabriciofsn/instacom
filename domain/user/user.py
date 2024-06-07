from shared.uuid.uuid import UuidGenerator
from domain.post.post import Post

class User(UuidGenerator):
  def __init__(self,name,user_name,birthday,email,password,following=None,followers=None, posts: Post=None):
    super().__init__()
    self._name = name
    self._user_name = user_name
    self._birthday = birthday
    self._email = email
    self._password = password
    self._following = following if following is not None else []
    self._followers = followers if followers is not None else []
    self._posts = posts
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self,name):
    self._name = name
  
  @property
  def user_name(self):
    return self._user_name
  
  @user_name.setter
  def user_name(self, user_name):
    self._user_name = user_name
  
  @property
  def birthday(self):
    return self._birthday
  
  @birthday.setter
  def birthday(self,birthday):
    self._birthday = birthday
  
  @property
  def email(self):
    return self._email
  
  @email.setter
  def email(self,email):
    self._email = email
  
  @property
  def password(self):
    return self._password
  
  @password.setter
  def password(self, password):
    self._password = password
  
  @property
  def following(self):
    return self._following
  
  @following.setter
  def following(self,following):
    self._following = following

  @property
  def followers(self):
    return self._followers
  
  @followers.setter
  def followers(self, followers):
    self._followers = followers

  @property 
  def posts(self):
    return self._posts
  
  @posts.setter
  def posts(self,posts):
    self._posts = posts