# SPDX-License-Identifier: MPL-2.0
# Copyright (C) 2021 Gemeente Amsterdam
from datapunt_api.rest import DisplayField, HALSerializer

from signals.apps.questionnaires.models import Questionnaire
from signals.apps.questionnaires.rest_framework.fields import (
    QuestionnairePublicHyperlinkedIdentityField
)
from signals.apps.questionnaires.rest_framework.serializers.public.questions import (
    PublicQuestionDetailedSerializer,
    PublicQuestionSerializer
)


class PublicQuestionnaireSerializer(HALSerializer):
    serializer_url_field = QuestionnairePublicHyperlinkedIdentityField

    _display = DisplayField()
    first_question = PublicQuestionSerializer()

    class Meta:
        model = Questionnaire
        fields = (
            '_links',
            '_display',
            'uuid',
            'name',
            'description',
            'is_active',
            'first_question'
        )
        read_only_fields = fields  # No create or update allowed


class PublicQuestionnaireDetailedSerializer(PublicQuestionnaireSerializer):
    first_question = PublicQuestionDetailedSerializer()