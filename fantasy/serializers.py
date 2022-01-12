from rest_framework import serializers
from .models import UserProfile, UserFPLCreate, UserFPLPick, Captain
from league.serializers import PlayerSerializer
from league.models import Player

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)  

    class Meta:
        model = UserProfile
        fields = "__all__"
    
    def get_user(self, obj):
        return obj.user.username 

class UserFPLCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFPLCreate
        fields = "__all__"

        extra_kwargs = {
            'user': {
                "read_only": True,
            }
        }
    
    def create(self, validated_data):
        gkp = validated_data.get("gpk1")
        gkp = validated_data.get("gkp1")
        def1 = validated_data.get("def1")
        def2 = validated_data.get("def2")
        def3 = validated_data.get("def3")
        def4 = validated_data.get("def4")
        mid1 = validated_data.get("mid1")
        mid2 = validated_data.get("mid2")
        mid3 = validated_data.get("mid3")
        att1 = validated_data.get("att1")
        att2 = validated_data.get("att2")
        att3 = validated_data.get("att3")
        gkp_bench = validated_data.get("gkp2")
        def_bench = validated_data.get("def5")
        mid_bench = validated_data.get("mid4")
        att_bench = validated_data.get("att4")
        fplcreate = UserFPLCreate.objects.create(**validated_data)
        fplcreate.save()
        fplpick = UserFPLPick.objects.create(
            user=fplcreate.user,
            gkp = gkp,
            def1 = def1,
            def2 = def2,
            def3 = def3,
            def4 = def4,
            mid1 = mid1,
            mid2 = mid2,
            mid3 = mid3,
            att1 = att1,
            att2 = att2,
            att3 = att3,
            gkp_bench = gkp_bench,
            def_bench = def_bench,
            mid_bench = mid_bench,
            att_bench = att_bench,
        )
        fplpick.save()
        captain, created = Captain.objects.get_or_create(user=fplcreate.user)
        captain.captain = mid2
        captain.save()
        return fplcreate

class UserViewTeamSerializer(serializers.ModelSerializer):
    gkp = PlayerSerializer(read_only=True)   
    def1 = PlayerSerializer(read_only=True)  
    def2 = PlayerSerializer(read_only=True)  
    def3 = PlayerSerializer(read_only=True)  
    def4 = PlayerSerializer(read_only=True)  
    mid1 = PlayerSerializer(read_only=True)  
    mid2 = PlayerSerializer(read_only=True)  
    mid3 = PlayerSerializer(read_only=True)  
    att1 = PlayerSerializer(read_only=True)  
    att2 = PlayerSerializer(read_only=True)  
    att3 = PlayerSerializer(read_only=True)  
    gkp_bench = PlayerSerializer(read_only=True)  
    def_bench = PlayerSerializer(read_only=True)   
    mid_bench = PlayerSerializer(read_only=True)  
    att_bench = PlayerSerializer(read_only=True)
    captain = serializers.SerializerMethodField(read_only=True)   
    class Meta:
        model = UserFPLPick
        exclude = ('user', )
    
    def get_captain(self, obj):
        captain = Captain.objects.get(user=obj.user)
        return PlayerSerializer(captain.captain).data

