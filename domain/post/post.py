from shared.uuid import UuidGenerator

class Post(UuidGenerator):
  def __init__(self,url_img,likes,comments):
    super().__init__()
    self.url = url_img
    self.likes = likes
    self.comments = comments