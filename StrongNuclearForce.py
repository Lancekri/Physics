def strongNuclearForce(n, z):
  return f"N/Z = {n/z} {str:{"Unstable" if (n/z > 1.1 or n/z < 1) else "Stable"}}"              

def main():
  input("Atomic Mass:")
