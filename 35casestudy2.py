# Text Compression Using Character Runs: Encode a string by grouping consecutive repeated characters and compare original 
# and encoded lengths, including cases where encoding is not beneficial. 
text = "aaabbccccdd"
compressed = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count = count + 1
    else:
        compressed = compressed + text[i - 1] + str(count)
        count = 1

if len(text) > 0:
    compressed = compressed + text[-1] + str(count)

print("Original text:", text)
print("Compressed text:", compressed)
print("Original length:", len(text))
print("Compressed length:", len(compressed))

if len(compressed) < len(text):
    print("Compression is beneficial")
else:
    print("Compression is not beneficial")