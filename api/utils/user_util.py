import base64
from django.contrib.auth.models import User
from api.models.seller_model import Seller
from api.models.branch_store_model import BranchStore

class UserUtil():
    
    def get_user_info(user_base64):
      try: 
        base64_bytes = user_base64.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        username, password = sample_string.split(":")
        user = User.objects.get(username=username)
        return user
      except User.DoesNotExist:
        return None
      

    def get_branch(user_id):
      seller = Seller.objects.get(user_id=user_id)
      branch_store = BranchStore.objects.get(seller=seller)
      return branch_store

