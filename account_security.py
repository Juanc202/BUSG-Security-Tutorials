def create_strong_password():
  """Creates a strong password."""
  password = ""
  for i in range(10):
    password += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
  return password

if __name__ == "__main__":
  print(create_strong_password())
