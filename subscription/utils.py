from subscription.models import Subscription, SubscriptionQuestionAllowence, SubscriptionQuestionCategory
from subscription.serializers import SubscriptionSerializer, GetSubscriptionSerializer, SubscriptionQuestionAllowenceSerializer
from exam.models import Exam
from exam.serializers import GetExamSerializer, ExamShortSerializer

def updateSubscription(new_obj, sid):
    try:
        subscription = Subscription.objects.get(id=sid)
        subscription.name = new_obj['subscription']['name']
        if new_obj['subscription'].get('days') == "":
            new_obj['subscription']['days'] = None
        if new_obj['subscription'].get('till_date') == "":
            new_obj['subscription']['till_date'] = None
        subscription.days = new_obj['subscription'].get('days')
        subscription.till_date = new_obj['subscription'].get('till_date')
        subscription.price = new_obj['subscription']['price']
        subscription.selling_points = new_obj['subscription']['selling_points']
        subscription.save()
        subscription_allowences = SubscriptionQuestionAllowence.objects.filter(subscription=subscription)
        new_allowence_ids = []
        new_allowence_objects = []
        for tmp_k in new_obj['question_number_allowence']:
            if tmp_k.get('id') is not None: new_allowence_ids.append(tmp_k.get('id'))
            else: new_allowence_objects.append(tmp_k)
        for i in subscription_allowences:
            if i.id in new_allowence_ids:
                new_tmp_obj = False
                tmp_count = 0
                while not new_tmp_obj: 
                    if i.id == new_obj['question_number_allowence'][tmp_count]['id']:
                        new_tmp_obj = new_obj['question_number_allowence'][tmp_count]
                i.category = SubscriptionQuestionCategory.objects.get(id=new_tmp_obj['question_number_allowence']['category']['id'])
                i.secondary_id = new_tmp_obj['question_number_allowence']['secondary_id']
                i.subject_name = new_tmp_obj['question_number_allowence']['subject_name']
                i.question_number = new_tmp_obj['question_number_allowence']['question_number']
                i.frequency = new_tmp_obj['question_number_allowence']['frequency']
                i.save()
            else:
                SubscriptionQuestionAllowence.objects.filter(id=i.id).delete()
        for new_i in new_allowence_objects:
            SubscriptionQuestionAllowence(subscription=subscription,category=SubscriptionQuestionCategory.objects.\
            get(id=new_i['category']['id']),secondary_id=new_i['secondary_id'],subject_name=new_i['subject_name'],\
            question_number=new_i['question_number'],frequency=new_i['frequency']).save()
        return {'result':True,"subscription":subscription}
    except KeyboardInterrupt: return {'result':False}

def createSubscription(new_obj):
    try:
        subscription_serializer = SubscriptionSerializer(data=new_obj['subscription'])
        if subscription_serializer.is_valid(): subscription_obj = subscription_serializer.save()
        for i in new_obj.get('question_number_allowence'):
            i['subscription'] = subscription_obj.id
            subs_que_allow_serializer = SubscriptionQuestionAllowenceSerializer(data=i)
            if subs_que_allow_serializer.is_valid(): subs_que_allow_serializer.save()
        exam = Exam.objects.filter(id=new_obj['subscription']['exam'])
        if not exam: return {"result":False}
        exam_details = GetExamSerializer(exam[0]).data
        all_subscription = Subscription.objects.filter(exam=exam[0])
        exam_details['exam_subscription'] = GetSubscriptionSerializer(all_subscription, many=True).data
        return {'result':True,"exam_details":exam_details}
    except KeyboardInterrupt: return {'result':False}

