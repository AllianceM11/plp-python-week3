scores = [72, 45, 90, 61, 38]

passed = 0
fail = 0

for score in scores:
  if score >= 80:
    print(score, "A")
  elif score >= 70:
    print(score, "B")
  elif score >= 50:
    print(score, "C")
else:
    print(score, "F")
