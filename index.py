from domain.user.user import User
from domain.post.post import Post
from datetime import datetime

post = Post("Conteúdo do Chiquinho")

user1 = User(
  name="Ripuda",
  user_name="ripuda_passaro",
  birthday=datetime(1994,5,25),
  email="ripuda_pai@gmail.com",
  password="ripuda123",
  following=["Rian", "Marta", "Kauane"],
  followers=["Rian"],
  posts=post
)

print(vars(user1))
