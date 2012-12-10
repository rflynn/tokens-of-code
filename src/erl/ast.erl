% parse myself, dump ast and print node cnt

-module(ast).
-export([parse/0]).

parse() ->
    {ok, Forms} = epp_dodger:parse_file(?FILE),
    io:format("Forms=~p~n", [Forms]),
    io:format("NodeCnt=~p~n",
        [lists:sum([erl_syntax_lib:fold(
            fun(_,N)-> N+1 end, 0, F) || F <- Forms])]).
