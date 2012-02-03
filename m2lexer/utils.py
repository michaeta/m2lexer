class TidGenerator(object):

    def __init__(self, max_tokens):
        self.MAX_TOKENS = max_tokens
        self.tid_gen = self._tid_generator(max_tokens)
    
    def _tid_generator(self, N):
        for i in xrange(N):
            yield i

    def generate_tid(self):
        return self.tid_gen.next()

