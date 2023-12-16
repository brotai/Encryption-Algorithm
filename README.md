# Encryption-Algorithm
A secure, easy to understand algorithm.

## Principles used:
- Symmetric keys: I have chosen to use The Vignère cipher principles
- One-time pads: I'm using pythons urandom function to craft the private key
- LZMA: Compression optional
- Multi-character chunking: Improved security by treating larger chunks of text as the characters of our message (Trigraphs)

  ### The downsides:
  - Python urandom function is not truly random. Python uses seeds to generate our key. 
  - Symmetric key algorithms are common, Most cryptoanalists will consider this fact if they wanted to crack into your files.
  - The size of your files generate a key of the same size. 1GB text file = 1GB private key.
