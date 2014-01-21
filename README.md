non-blocking-pipe
=================

A wrapper tool to make linux pipe non-blocking

# Introduction

Linux pipe is a light and powerful tool to bind programs together. For example, [this post](http://adam.heroku.com/past/2011/4/1/logs_are_streams_not_files/) suggest to treat log as stream, linux pipe make it possible to redirect it to any consumer.


But, linux pipe has a problem in practice, for a binding like 'A | B', if B got stuck for whatever reason, as long as it doesn't read from stdin, os would hang up A after the buffer between A and B are filled up. In the situation A is a product program, while B is a log redirector like logstash, that would bring serious problem.


While A should not be blocked, the overflowed data to B should be discarded. This non-blocking-pipe is introduced to do that with usage:

    A | non-blocking-pipe B b-arg1 b-arg2 ...

