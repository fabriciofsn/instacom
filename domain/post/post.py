from shared.uuid.uuid import UuidGenerator

class Post(UuidGenerator):
  def __init__(self,url_img=None,likes=None,comments=None):
    super().__init__()
    self.url = url_img
    self.likes = likes
    self.comments = comments if comments is not None else []