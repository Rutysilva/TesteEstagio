def q2_contar_frequenciaa_palavra(text):
    num_rep_hello = 0;
    num_rep_word = 0;
    
    for name in text.split():
        if name == "Hello" or name == "hello":
            num_rep_hello = num_rep_hello + 1
        if name == "World" or name == "world":
            num_rep_word = num_rep_word +1
    print(f'Hello: {num_rep_hello} World: {num_rep_word}')
 


text = 'Hello world hello'
print(q2_contar_frequenciaa_palavra(text))