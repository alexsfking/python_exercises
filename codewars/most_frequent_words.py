import re

pattern = re.compile(r"[a-zA-Z']+")

def top_3_words(text:str)->list[str]:
    words_dict=dict()
    matches=pattern.findall(text)
    for match in matches:
        if(match.count("'")!=len(match)):
            word=match.lower()
            words_dict[word] = words_dict.get(word, 0) + 1
    sorted_words=sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    return [w[0] for w in sorted_words[:3]]

print(top_3_words("HUeUcAv_-HUeUcAv//?qjexSlKIK?qjexSlKIK/. /_e'xXGEG?;_Cfqbns!Cfqbns,/__GZekdwRBN .,e'xXGEG?UpB,!qjexSlKIK_!GZekdwRBN-_.UpB!!, !UpB  .:;UpB! ;HUeUcAv;CuQkmjq ;:Cfqbns : _Cfqbns!?/:?GZekdwRBN?CuQkmjq_: _GZekdwRBN;?UpB?:_Cfqbns.GZekdwRBN;HUeUcAv?,!Cfqbns?./UpB:CuQkmjq/,GZekdwRBN!,/e'xXGEG:,_:GZekdwRBN;Cfqbns.-?UpB/,/CuQkmjq..GZekdwRBN:UpB?e'xXGEG :;:!qjexSlKIK?!-qjexSlKIK?_ /!Cfqbns,_e'xXGEG--,GZekdwRBN?//_HUeUcAv_e'xXGEG/Cfqbns:,,-_e'xXGEG ??e'xXGEG?;;GZekdwRBN-.?-Cfqbns/Cfqbns,,,/Cfqbns!_;/-UpB_Cfqbns!UpB- -;!e'xXGEG-!HUeUcAv ;!qjexSlKIK !,HUeUcAv!?-HUeUcAv!/-UpB-,,/-Cfqbns;_/;_qjexSlKIK?e'xXGEG_-?GZekdwRBN, ?- qjexSlKIK?qjexSlKIK GZekdwRBN,-GZekdwRBN!_!!.Cfqbns!,?;qjexSlKIK.-jqHnVk/: /_qjexSlKIK:GZekdwRBN. _;!UpB?/ ._e'xXGEG.,Cfqbns-,.,HUeUcAv_GZekdwRBN-:!UpB,?UpB-:./;e'xXGEG,qjexSlKIK?:;e'xXGEG,-!HUeUcAv!.--CuQkmjq_Cfqbns? ;?;GZekdwRBN/ CuQkmjq-qjexSlKIK-e'xXGEG ? ?/HUeUcAv_!!,Cfqbns!??/ GZekdwRBN_-:,_HUeUcAv?,GZekdwRBN-;!CuQkmjq!.HUeUcAv_ !/Cfqbns/:;GZekdwRBN/e'xXGEG!.._HUeUcAv ?qjexSlKIK /__!UpB!/qjexSlKIK/qjexSlKIK_; qjexSlKIK._?HUeUcAv. /._HUeUcAv_/Cfqbns;;-;!e'xXGEG /;:GZekdwRBN;:-_e'xXGEG.e'xXGEG ;:Cfqbns;CuQkmjq:?:.Cfqbns///,qjexSlKIK!-,/qjexSlKIK?;Cfqbns;_GZekdwRBN _ -?Cfqbns_:/;jqHnVk  ; :e'xXGEG-- :?HUeUcAv-CuQkmjq!! Cfqbns,_,.:GZekdwRBN. Cfqbns.-;/;HUeUcAv:e'xXGEG? CuQkmjq,GZekdwRBN,._..UpB;---/CuQkmjq!:e'xXGEG_!HUeUcAv. qjexSlKIK:_HUeUcAv-e'xXGEG!UpB-_:/.e'xXGEG?CuQkmjq::,qjexSlKIK;.!?HUeUcAv;,;!HUeUcAv!/GZekdwRBN ,:e'xXGEG:;HUeUcAv/,-?Cfqbns/qjexSlKIK_,GZekdwRBN?-! CuQkmjq;!! CuQkmjq--.Cfqbns ?e'xXGEG!//UpB,HUeUcAv!!Cfqbns?HUeUcAv.;-_e'xXGEG_- ;-CuQkmjq/,Cfqbns:!-HUeUcAv-:_:-UpB-UpB;!HUeUcAv_ .-"))