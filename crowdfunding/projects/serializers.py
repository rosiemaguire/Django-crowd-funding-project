from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
  supporter = serializers.ReadOnlyField(source='supporter.id')
  class Meta:
    model = apps.get_model('projects.Pledge')
    fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.id')
  class Meta:        
    model = apps.get_model('projects.Project')        
    fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
  pledges = PledgeSerializer(many=True)

  def update(self,instance,validated_data):
    if instance.is_open:
      instance.title = validated_data.get('title', instance.title)
      instance.description = validated_data.get('description', instance.description)
      instance.goal = validated_data.get('goal', instance.goal)
      instance.image = validated_data.get('image', instance.image)
      instance.is_open = validated_data.get('is_open', instance.is_open)
      instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
      if instance.is_deleted == True:
        instance.is_open = False
        for pledge in instance.pledges.all():
          pledge.is_deleted = True
          pledge.save()
      instance.save()
    else:
      instance.is_open = validated_data.get('is_open',instance.is_open)
      instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
      instance.save()
    return instance
  
class PledgeDetailSerializer(PledgeSerializer):

  def update(self,instance,validated_data):
    instance.comment = validated_data.get('comment', instance.comment)
    instance.anonymous = validated_data.get('anonymous', instance.anonymous)
    instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
    instance.save()
    return instance
