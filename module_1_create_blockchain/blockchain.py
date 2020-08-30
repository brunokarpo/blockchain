import datetime
import hashlab
import json
from flask import Flask, jsonify

# Part 1 - Create a blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash='0')