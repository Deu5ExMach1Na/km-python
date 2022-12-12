import hashlib
def get_sigcode(data):
  raw=f"data={data}maomi_pass_xyz"
  hashl=hashlib.md5()
  hashl.update(raw.encode("Utf-8"))
  return hashl.hexdigest().lower()