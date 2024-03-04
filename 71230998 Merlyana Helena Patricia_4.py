#!/usr/bin/env python
# coding: utf-8

# In[2]:


def cek_angka(pertama, kedua, ketiga):
    if pertama != kedua and pertama != ketiga and kedua != ketiga:
        if pertama == kedua + ketiga or kedua == pertama + ketiga or ketiga == kedua + ketiga:
            return True 
        return False
    
print(cek_angka(10, 20,30))


# In[8]:


def cek_digit_belakang():
    kesatu1 = int(input("Input angka pertama: "))
    kedua2 = int(input("input angka kedua: "))
    ketiga3 = int(input("Input angka ketiga: "))
    
    cek_angka1 = kesatu1 % 10
    cek_angka2 = kedua2 % 10
    cek_angka3 = ketiga3 % 10
    
    if (cek_angka1 == cek_angka2) or (cek_angka1 == cek_angka3) or (cek_angka2 == cek_angka3):
        return True
    else: 
        return False
    
print(cek_digit_belakang())


# In[10]:


c_to_f = lambda c: (9/5) * c + 32
c_to_r = lambda c: 0.8 * c

print(c_to_f(100))
print(c_to_r(80))


# In[ ]:




