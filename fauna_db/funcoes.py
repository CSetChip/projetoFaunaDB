from faunadb import query as q
from faunadb.client import FaunaClient

client = FaunaClient(secret='fnAFSwNWqYAAQvPaevygUZbdw9jB5JknZ7fmxIfm')

def criar_documento(collection_name, data):
    return client.query(
        q.create(
            q.collection(collection_name),
            {'data': data}
        )
    )

def obter_documento(collection_name, document_id):
    return client.query(
        q.get(
            q.ref(
                q.collection(collection_name),
                document_id
            )
        )
    )

def atualizar_documento(collection_name, document_id, novos_dados):
    return client.query(
        q.update(
            q.ref(
                q.collection(collection_name),
                document_id
            ),
            {'data': novos_dados}
        )
    )

def deletar_documento(collection_name, document_id):
    return client.query(
        q.delete(
            q.ref(
                q.collection(collection_name),
                document_id
            )
        )
    )
