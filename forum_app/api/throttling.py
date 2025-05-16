from rest_framework.throttling import UserRateThrottle


class QuestionThrottle(UserRateThrottle):
    scope = 'question'

    def allow_request(self, request, view):

        if request.method == 'GET':
            return True

        new_scope = 'question-' + request.method.lower()
        if new_scope in self.THROTTLE_RATES:
            self.scope = new_scope
            self.rate = self.get_rate()
            self.num_requests, self.duration = self.aprse_rate(self.rate)
            print(self.scope)

        return super().allow_request(request, view)


class QuestionGetThrottle(UserRateThrottle):
    scope = 'question-get'


class QuestionPostThrottle(UserRateThrottle):
    scope = 'question-post'
