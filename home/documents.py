from django_elasticsearch_dsl import (
    Document ,
    fields,
    Index,
)
from .models import ElasticDemo
PUBLISHER_INDEX = Index('elastic_demo')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)




@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    
    id = fields.IntegerField(attr='id')
    fielddata=True
    title = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    content = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
   

    class Django(object):
        model = ElasticDemo