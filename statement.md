# Problem Statement

Most people underestimate how vulnerable their everyday digital habits are.
Weak or reused passwords, skipped two-factor authentication, and casual
oversharing online are all common, and most people have never seen, in
concrete terms, how quickly these weaknesses can be exploited. Separately,
secure communication depends on two parties being able to agree on a secret
key without ever transmitting that key directly - a problem elegantly
solved by the Diffie-Hellman key exchange, but one whose mechanics are
rarely made visible or hands-on.

CyberGuard addresses both gaps in a single toolkit: it lets a user assess
their own password and digital footprint risk, walks them through a real,
working Diffie-Hellman key exchange used to encrypt an actual message, and
then - from an attacker's perspective - demonstrates exactly how weak
passwords, small keys, and unkeyed ciphers get broken, tying the "why this
matters" back to the habits and choices assessed earlier.

## Scope

The project is a single-user, offline, GUI desktop application. It does not
connect to real networks, does not store or transmit any real user data,
and uses only small, deliberately toy-sized numbers for its cryptographic
demonstrations (suitable for teaching the underlying concepts, not for
real-world security use). All cryptography (Diffie-Hellman, Caesar cipher,
Atbash cipher) is implemented from first principles using core Python only,
without external cryptography libraries.

## Target Users

- Students learning the fundamentals of cybersecurity, cryptography, or
  ethical hacking
- Anyone who wants a concrete, interactive sense of why password strength,
  two-factor authentication, and key size actually matter
- Instructors or reviewers evaluating a hands-on demonstration of
  Diffie-Hellman key exchange and classical ciphers

## High-Level Features

1. **Password & Digital Footprint Check** - scores password strength and
   overall digital-habit risk
2. **Secure Key Exchange & Encryption** - a working Diffie-Hellman exchange
   between two simulated parties, whose resulting shared secret is used to
   encrypt and decrypt a real message with a Caesar or Atbash cipher
3. **Ethical Hacking Attack Simulator** - brute-force attacks against a
   weak password, a small Diffie-Hellman prime, and a Caesar cipher, plus
   instant decryption of an Atbash cipher, demonstrating in practice why
   the choices in modules 1 and 2 matter
