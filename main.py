from blockchain import  BlockChain
from flask import Flask, jsonify

app= Flask(__name__)
blockchain= BlockChain()

@app.route('/mine_block',methods=['GET'])
def mine_block():
    previous_block=blockchain.get_previous_block()
    previous_proof=previous_block['proof']
    proof=blockchain.proof_of_work(previous_proof)
    previous_hash=blockchain.hash(previous_block)
    block=blockchain.create_block(proof,previous_hash)
    response={'message':'you just mined a block',
              'index':block['index'],
              'timestamp':block['timestamp'],
              'proof':block['proof'],
              'previous_hash':block['previous_hash']}
    return jsonify(response),200

@app.route('/get_chain',methods=['GET'])
def get_chain():
    response={'chain':blockchain.chain,
              'length':len(blockchain.chain)}
    return jsonify(response),200

@app.route('/is_valid',methods=['GET'])
def is_valid():
    is_valid=blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response={'message':'The block chain is valid'}
    else:
        response={'message':'The block chain is not valid'}
    return jsonify(response), 200

app.run(host="127.0.0.1",port="8080")
