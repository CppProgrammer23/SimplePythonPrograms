import random

#constants
ALPHABET=[chr(x) for x in range(65,91)]
NONCE=[1,2,3]

class Student:
  def __init__(self):
    self.hash=random.randint(120,215)

  def addStudent(self,subject,pID,grade):
    if subject[0].upper() not in ALPHABET or pID[0].upper() not in ALPHABET:
      raise Exception('Verify your entries')
    print(f'\t\t\tPrevious Hash: {self.hash}')
    a=ord(subject[0].upper())
    b=ord(pID[0].upper())
    c=ord(grade)
    val=int(str(self.hash)[-2:])
    temp=a+b+c-val
    #find the hash and store it in self.hash
    for nonce in NONCE:
      if (nonce+temp)%3==0:
        self.hash=nonce+temp
        break
    print(f'Subject: {subject}, {pID},grade: {grade},nonce: {nonce},\
    Hash: {self.hash}')


s=Student()
for i in range(3):
  sub=input('Enter the subject: ')
  pid=input('Enter the ID: ')
  g=input('Enter the grade: ')
  s.addStudent(sub,pid,g)
