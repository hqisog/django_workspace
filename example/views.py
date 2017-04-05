from django.http import Http404, HttpResponse
from .models import Poem


def more_poems(request):
    if request.is_ajax():
        objects = Poem.objects.all()
        #[{author:'allen',title:'1'},{}]
        data = get_json_objects(objects, Poem)
        print(data)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404

def json_filed(field_data):
    if isinstance(field_data, str):
        return "\"" + field_data + "\""
    if isinstance(field_data, bool):
        if field_data == 'False':
            return 'false'
        else:
            return 'true'
    return str(field_data)

def json_encode_dict(dict_data):
    json_data = "{"
    for (k,v) in dict_data.items():
        json_data = json_data +json_filed(k) + ": " + json_filed(v) + ", "
    json_data = json_data[:-2] + "}"
    print json_data
    return json_data

def json_encode_list(list_data):
    json_res = "["
    for item in list_data:
        json_res = json_res + json_encode_dict(item) + ", "

    return json_res[:-2] + "]"

def get_json_objects(objects, model_meta):
    concrete_model = Poem._meta.concrete_model
    list_data = []
    for obj in objects:
        dict_data = {}
        for field in concrete_model._meta.local_fields:
            if field.name == 'id':
                continue
            value = field.value_from_object(obj)
            dict_data[field.name] = value

        list_data.append(dict_data)

    data = json_encode_list(list_data)
    return data

import ast

def add(request):
    if request.is_ajax() and request.POST:
        json_str = request.POST.get('poems')
        data = "post success"
        json_list = ast.literal_eval(json_str)
        for item in json_list:
            new_obj = Poem()
            # for filed in item:
                # p1=Poem.objects().create(filed=str(item[filed]))
            new_obj.author=item.get('author','')
            new_obj.title=item.get('title','')
            new_obj.poem_id=item.get('poem_id','')
            new_obj.save()
                # setattr(new_obj, filed, item[filed])
            print(new_obj.author, new_obj.title, new_obj.poem_id)
            # new_obj.save()
        return HttpResponse(data, content_type='application/text')
    else:
        return Http404
    