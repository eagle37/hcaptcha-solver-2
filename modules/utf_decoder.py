def unicode_Coversion(findUtf):
    unicode_Letters = [
    [ ['ɑ', b'\xc9\x91'], ['α', b'\xce\xb1'], ['а', b'\xd0\xb0'], ['⍺', b'\xe2\x8d\xba'], ['𝐚', b'\xf0\x9d\x90\x9a'], ['𝑎', b'\xf0\x9d\x91\x8e'], ['𝒂', b'\xf0\x9d\x92\x82'], ['𝒶', b'\xf0\x9d\x92\xb6'], ['𝓪', b'\xf0\x9d\x93\xaa'], ['𝔞', b'\xf0\x9d\x94\x9e'], ['𝕒', b'\xf0\x9d\x95\x92'], ['𝖆', b'\xf0\x9d\x96\x86'], ['𝖺', b'\xf0\x9d\x96\xba'], ['𝗮', b'\xf0\x9d\x97\xae'], ['𝘢', b'\xf0\x9d\x98\xa2'], ['𝙖', b'\xf0\x9d\x99\x96'], ['𝚊', b'\xf0\x9d\x9a\x8a'], ['𝛂', b'\xf0\x9d\x9b\x82'], ['𝛼', b'\xf0\x9d\x9b\xbc'], ['𝜶', b'\xf0\x9d\x9c\xb6'], ['𝝰', b'\xf0\x9d\x9d\xb0'], ['𝞪', b'\xf0\x9d\x9e\xaa'], ['ａ', b'\xef\xbd\x81']],
    [ ['Ƅ', b'\xc6\x84'], ['Ь', b'\xd0\xac'], ['Ꮟ', b'\xe1\x8f\x8f'], ['ᑲ', b'\xe1\x91\xb2'], ['ᖯ', b'\xe1\x96\xaf'], ['𝐛', b'\xf0\x9d\x90\x9b'], ['𝑏', b'\xf0\x9d\x91\x8f'], ['𝒃', b'\xf0\x9d\x92\x83'], ['𝒷', b'\xf0\x9d\x92\xb7'], ['𝓫', b'\xf0\x9d\x93\xab'], ['𝔟', b'\xf0\x9d\x94\x9f'], ['𝕓', b'\xf0\x9d\x95\x93'], ['𝖇', b'\xf0\x9d\x96\x87'], ['𝖻', b'\xf0\x9d\x96\xbb'], ['𝗯', b'\xf0\x9d\x97\xaf'], ['𝘣', b'\xf0\x9d\x98\xa3'], ['𝙗', b'\xf0\x9d\x99\x97'], ['𝚋', b'\xf0\x9d\x9a\x8b']],
    [ ['ϲ', b'\xcf\xb2'], ['с', b'\xd1\x81'], ['ᴄ', b'\xe1\xb4\x84'], ['ⅽ', b'\xe2\x85\xbd'], ['ⲥ', b'\xe2\xb2\xa5'], ['ꮯ', b'\xea\xae\xaf'], ['𐐽', b'\xf0\x90\x90\xbd'], ['𝐜', b'\xf0\x9d\x90\x9c'], ['𝑐', b'\xf0\x9d\x91\x90'], ['𝒄', b'\xf0\x9d\x92\x84'], ['𝒸', b'\xf0\x9d\x92\xb8'], ['𝓬', b'\xf0\x9d\x93\xac'], ['𝔠', b'\xf0\x9d\x94\xa0'], ['𝕔', b'\xf0\x9d\x95\x94'], ['𝖈', b'\xf0\x9d\x96\x88'], ['𝖼', b'\xf0\x9d\x96\xbc'], ['𝗰', b'\xf0\x9d\x97\xb0'], ['𝘤', b'\xf0\x9d\x98\xa4'], ['𝙘', b'\xf0\x9d\x99\x98'], ['𝚌', b'\xf0\x9d\x9a\x8c'], ['ｃ', b'\xef\xbd\x83']],
    [ ['ԁ', b'\xd4\x81'], ['Ꮷ', b'\xe1\x8f\xa7'], ['ᑯ', b'\xe1\x91\xaf'], ['ⅆ', b'\xe2\x85\x86'], ['ⅾ', b'\xe2\x85\xbe'], ['ꓒ', b'\xea\x93\x92'], ['𝐝', b'\xf0\x9d\x90\x9d'], ['𝑑', b'\xf0\x9d\x91\x91'], ['𝒅', b'\xf0\x9d\x92\x85'], ['𝒹', b'\xf0\x9d\x92\xb9'], ['𝓭', b'\xf0\x9d\x93\xad'], ['𝔡', b'\xf0\x9d\x94\xa1'], ['𝕕', b'\xf0\x9d\x95\x95'], ['𝖉', b'\xf0\x9d\x96\x89'], ['𝖽', b'\xf0\x9d\x96\xbd'], ['𝗱', b'\xf0\x9d\x97\xb1'], ['𝘥', b'\xf0\x9d\x98\xa5'], ['𝙙', b'\xf0\x9d\x99\x99'], ['𝚍', b'\xf0\x9d\x9a\x8d']],
    [ ['е', b'\xd0\xb5'], ['ҽ', b'\xd2\xbd'], ['℮', b'\xe2\x84\xae'], ['ℯ', b'\xe2\x84\xaf'], ['ⅇ', b'\xe2\x85\x87'], ['ꬲ', b'\xea\xac\xb2'], ['𝐞', b'\xf0\x9d\x90\x9e'], ['𝑒', b'\xf0\x9d\x91\x92'], ['𝒆', b'\xf0\x9d\x92\x86'], ['𝓮', b'\xf0\x9d\x93\xae'], ['𝔢', b'\xf0\x9d\x94\xa2'], ['𝕖', b'\xf0\x9d\x95\x96'], ['𝖊', b'\xf0\x9d\x96\x8a'], ['𝖾', b'\xf0\x9d\x96\xbe'], ['𝗲', b'\xf0\x9d\x97\xb2'], ['𝘦', b'\xf0\x9d\x98\xa6'], ['𝙚', b'\xf0\x9d\x99\x9a'], ['𝚎', b'\xf0\x9d\x9a\x8e'], ['ｅ', b'\xef\xbd\x85']],
    [ ['ſ', b'\xc5\xbf'], ['ք', b'\xd6\x84'], ['ẝ', b'\xe1\xba\x9d'], ['ꞙ', b'\xea\x9e\x99'], ['ꬵ', b'\xea\xac\xb5'], ['𝐟', b'\xf0\x9d\x90\x9f'], ['𝑓', b'\xf0\x9d\x91\x93'], ['𝒇', b'\xf0\x9d\x92\x87'], ['𝒻', b'\xf0\x9d\x92\xbb'], ['𝓯', b'\xf0\x9d\x93\xaf'], ['𝔣', b'\xf0\x9d\x94\xa3'], ['𝕗', b'\xf0\x9d\x95\x97'], ['𝖋', b'\xf0\x9d\x96\x8b'], ['𝖿', b'\xf0\x9d\x96\xbf'], ['𝗳', b'\xf0\x9d\x97\xb3'], ['𝘧', b'\xf0\x9d\x98\xa7'], ['𝙛', b'\xf0\x9d\x99\x9b'], ['𝚏', b'\xf0\x9d\x9a\x8f']],
    [ ['ƍ', b'\xc6\x8d'], ['ɡ', b'\xc9\xa1'], ['ց', b'\xd6\x81'], ['ᶃ', b'\xe1\xb6\x83'], ['ℊ', b'\xe2\x84\x8a'], ['𝐠', b'\xf0\x9d\x90\xa0'], ['𝑔', b'\xf0\x9d\x91\x94'], ['𝒈', b'\xf0\x9d\x92\x88'], ['𝓰', b'\xf0\x9d\x93\xb0'], ['𝔤', b'\xf0\x9d\x94\xa4'], ['𝕘', b'\xf0\x9d\x95\x98'], ['𝖌', b'\xf0\x9d\x96\x8c'], ['𝗀', b'\xf0\x9d\x97\x80'], ['𝗴', b'\xf0\x9d\x97\xb4'], ['𝘨', b'\xf0\x9d\x98\xa8'], ['𝙜', b'\xf0\x9d\x99\x9c'], ['𝚐', b'\xf0\x9d\x9a\x90'], ['ｇ', b'\xef\xbd\x87']],
    [ ['һ', b'\xd2\xbb'], ['հ', b'\xd5\xb0'], ['Ꮒ', b'\xe1\x8f\x82'], ['ℎ', b'\xe2\x84\x8e'], ['𝐡', b'\xf0\x9d\x90\xa1'], ['𝒉', b'\xf0\x9d\x92\x89'], ['𝒽', b'\xf0\x9d\x92\xbd'], ['𝓱', b'\xf0\x9d\x93\xb1'], ['𝔥', b'\xf0\x9d\x94\xa5'], ['𝕙', b'\xf0\x9d\x95\x99'], ['𝖍', b'\xf0\x9d\x96\x8d'], ['𝗁', b'\xf0\x9d\x97\x81'], ['𝗵', b'\xf0\x9d\x97\xb5'], ['𝘩', b'\xf0\x9d\x98\xa9'], ['𝙝', b'\xf0\x9d\x99\x9d'], ['𝚑', b'\xf0\x9d\x9a\x91'], ['ｈ', b'\xef\xbd\x88']],
    [ ['ı', b'\xc4\xb1'], ['ɩ', b'\xc9\xa9'], ['ɪ', b'\xc9\xaa'], ['˛', b'\xcb\x9b'], ['ͺ', b'\xcd\xba'], ['ι', b'\xce\xb9'], ['і', b'\xd1\x96'], ['ӏ', b'\xd3\x8f'], ['Ꭵ', b'\xe1\x8e\xa5'], ['ι', b'\xe1\xbe\xbe'], ['ℹ', b'\xe2\x84\xb9'], ['ⅈ', b'\xe2\x85\x88'], ['ⅰ', b'\xe2\x85\xb0'], ['⍳', b'\xe2\x8d\xb3'], ['ꙇ', b'\xea\x99\x87'], ['ꭵ', b'\xea\xad\xb5'], ['𑣃', b'\xf0\x91\xa3\x83'], ['𝐢', b'\xf0\x9d\x90\xa2'], ['𝑖', b'\xf0\x9d\x91\x96'], ['𝒊', b'\xf0\x9d\x92\x8a'], ['𝒾', b'\xf0\x9d\x92\xbe'], ['𝓲', b'\xf0\x9d\x93\xb2'], ['𝔦', b'\xf0\x9d\x94\xa6'], ['𝕚', b'\xf0\x9d\x95\x9a'], ['𝖎', b'\xf0\x9d\x96\x8e'], ['𝗂', b'\xf0\x9d\x97\x82'], ['𝗶', b'\xf0\x9d\x97\xb6'], ['𝘪', b'\xf0\x9d\x98\xaa'], ['𝙞', b'\xf0\x9d\x99\x9e'], ['𝚒', b'\xf0\x9d\x9a\x92'], ['𝚤', b'\xf0\x9d\x9a\xa4'], ['𝛊', b'\xf0\x9d\x9b\x8a'], ['𝜄', b'\xf0\x9d\x9c\x84'], ['𝜾', b'\xf0\x9d\x9c\xbe'], ['𝝸', b'\xf0\x9d\x9d\xb8'], ['𝞲', b'\xf0\x9d\x9e\xb2'], ['ｉ', b'\xef\xbd\x89']],
    [ ['ϳ', b'\xcf\xb3'], ['ј', b'\xd1\x98'], ['ⅉ', b'\xe2\x85\x89'], ['𝐣', b'\xf0\x9d\x90\xa3'], ['𝑗', b'\xf0\x9d\x91\x97'], ['𝒋', b'\xf0\x9d\x92\x8b'], ['𝒿', b'\xf0\x9d\x92\xbf'], ['𝓳', b'\xf0\x9d\x93\xb3'], ['𝔧', b'\xf0\x9d\x94\xa7'], ['𝕛', b'\xf0\x9d\x95\x9b'], ['𝖏', b'\xf0\x9d\x96\x8f'], ['𝗃', b'\xf0\x9d\x97\x83'], ['𝗷', b'\xf0\x9d\x97\xb7'], ['𝘫', b'\xf0\x9d\x98\xab'], ['𝙟', b'\xf0\x9d\x99\x9f'], ['𝚓', b'\xf0\x9d\x9a\x93'], ['ｊ', b'\xef\xbd\x8a']],
    [ ['𝐤', b'\xf0\x9d\x90\xa4'], ['𝑘', b'\xf0\x9d\x91\x98'], ['𝒌', b'\xf0\x9d\x92\x8c'], ['𝓀', b'\xf0\x9d\x93\x80'], ['𝓴', b'\xf0\x9d\x93\xb4'], ['𝔨', b'\xf0\x9d\x94\xa8'], ['𝕜', b'\xf0\x9d\x95\x9c'], ['𝖐', b'\xf0\x9d\x96\x90'], ['𝗄', b'\xf0\x9d\x97\x84'], ['𝗸', b'\xf0\x9d\x97\xb8'], ['𝘬', b'\xf0\x9d\x98\xac'], ['𝙠', b'\xf0\x9d\x99\xa0'], ['𝚔', b'\xf0\x9d\x9a\x94']],
    [ ['Ɩ', b'\xc6\x96'], ['ǀ', b'\xc7\x80'], ['Ι', b'\xce\x99'], ['І', b'\xd0\x86'], ['Ӏ', b'\xd3\x80'], ['׀', b'\xd7\x80'], ['ו', b'\xd7\x95'], ['ן', b'\xd7\x9f'], ['ا', b'\xd8\xa7'], ['١', b'\xd9\xa1'], ['۱', b'\xdb\xb1'], ['ߊ', b'\xdf\x8a'], ['ᛁ', b'\xe1\x9b\x81'], ['ℐ', b'\xe2\x84\x90'], ['ℑ', b'\xe2\x84\x91'], ['ℓ', b'\xe2\x84\x93'], ['Ⅰ', b'\xe2\x85\xa0'], ['ⅼ', b'\xe2\x85\xbc'], ['∣', b'\xe2\x88\xa3'], ['⏽', b'\xe2\x8f\xbd'], ['Ⲓ', b'\xe2\xb2\x92'], ['ⵏ', b'\xe2\xb5\x8f'], ['ꓲ', b'\xea\x93\xb2'], ['𐊊', b'\xf0\x90\x8a\x8a'], ['𐌉', b'\xf0\x90\x8c\x89'], ['𐌠', b'\xf0\x90\x8c\xa0'], ['𖼨', b'\xf0\x96\xbc\xa8'], ['𝐈', b'\xf0\x9d\x90\x88'], ['𝐥', b'\xf0\x9d\x90\xa5'], ['𝐼', b'\xf0\x9d\x90\xbc'], ['𝑙', b'\xf0\x9d\x91\x99'], ['𝑰', b'\xf0\x9d\x91\xb0'], ['𝒍', b'\xf0\x9d\x92\x8d'], ['𝓁', b'\xf0\x9d\x93\x81'], ['𝓘', b'\xf0\x9d\x93\x98'], ['𝓵', b'\xf0\x9d\x93\xb5'], ['𝔩', b'\xf0\x9d\x94\xa9'], ['𝕀', b'\xf0\x9d\x95\x80'], ['𝕝', b'\xf0\x9d\x95\x9d'], ['𝕴', b'\xf0\x9d\x95\xb4'], ['𝖑', b'\xf0\x9d\x96\x91'], ['𝖨', b'\xf0\x9d\x96\xa8'], ['𝗅', b'\xf0\x9d\x97\x85'], ['𝗜', b'\xf0\x9d\x97\x9c'], ['𝗹', b'\xf0\x9d\x97\xb9'], ['𝘐', b'\xf0\x9d\x98\x90'], ['𝘭', b'\xf0\x9d\x98\xad'], ['𝙄', b'\xf0\x9d\x99\x84'], ['𝙡', b'\xf0\x9d\x99\xa1'], ['𝙸', b'\xf0\x9d\x99\xb8'], ['𝚕', b'\xf0\x9d\x9a\x95'], ['𝚰', b'\xf0\x9d\x9a\xb0'], ['𝛪', b'\xf0\x9d\x9b\xaa'], ['𝜤', b'\xf0\x9d\x9c\xa4'], ['𝝞', b'\xf0\x9d\x9d\x9e'], ['𝞘', b'\xf0\x9d\x9e\x98'], ['𝟏', b'\xf0\x9d\x9f\x8f'], ['𝟙', b'\xf0\x9d\x9f\x99'], ['𝟣', b'\xf0\x9d\x9f\xa3'], ['𝟭', b'\xf0\x9d\x9f\xad'], ['𝟷', b'\xf0\x9d\x9f\xb7'], ['𞣇', b'\xf0\x9e\xa3\x87'], ['𞸀', b'\xf0\x9e\xb8\x80'], ['𞺀', b'\xf0\x9e\xba\x80'], ['🯱', b'\xf0\x9f\xaf\xb1'], ['ﺍ', b'\xef\xba\x8d'], ['ﺎ', b'\xef\xba\x8e'], ['Ｉ', b'\xef\xbc\xa9'], ['ｌ', b'\xef\xbd\x8c'], ['￨', b'\xef\xbf\xa8']],
    [ ['ⅿ', b'\xe2\x85\xbf'], ['𑜀', b'\xf0\x91\x9c\x80'], ['𑣣', b'\xf0\x91\xa3\xa3'], ['𝐦', b'\xf0\x9d\x90\xa6'], ['𝑚', b'\xf0\x9d\x91\x9a'], ['𝒎', b'\xf0\x9d\x92\x8e'], ['𝓂', b'\xf0\x9d\x93\x82'], ['𝓶', b'\xf0\x9d\x93\xb6'], ['𝔪', b'\xf0\x9d\x94\xaa'], ['𝕞', b'\xf0\x9d\x95\x9e'], ['𝖒', b'\xf0\x9d\x96\x92'], ['𝗆', b'\xf0\x9d\x97\x86'], ['𝗺', b'\xf0\x9d\x97\xba'], ['𝘮', b'\xf0\x9d\x98\xae'], ['𝙢', b'\xf0\x9d\x99\xa2'], ['𝚖', b'\xf0\x9d\x9a\x96']],
    [ ['ո', b'\xd5\xb8'], ['ռ', b'\xd5\xbc'], ['𝐧', b'\xf0\x9d\x90\xa7'], ['𝑛', b'\xf0\x9d\x91\x9b'], ['𝒏', b'\xf0\x9d\x92\x8f'], ['𝓃', b'\xf0\x9d\x93\x83'], ['𝓷', b'\xf0\x9d\x93\xb7'], ['𝔫', b'\xf0\x9d\x94\xab'], ['𝕟', b'\xf0\x9d\x95\x9f'], ['𝖓', b'\xf0\x9d\x96\x93'], ['𝗇', b'\xf0\x9d\x97\x87'], ['𝗻', b'\xf0\x9d\x97\xbb'], ['𝘯', b'\xf0\x9d\x98\xaf'], ['𝙣', b'\xf0\x9d\x99\xa3'], ['𝚗', b'\xf0\x9d\x9a\x97']],
    [ ['ο', b'\xce\xbf'], ['σ', b'\xcf\x83'], ['о', b'\xd0\xbe'], ['օ', b'\xd6\x85'], ['ס', b'\xd7\xa1'], ['ه', b'\xd9\x87'], ['٥', b'\xd9\xa5'], ['ھ', b'\xda\xbe'], ['ہ', b'\xdb\x81'], ['ە', b'\xdb\x95'], ['۵', b'\xdb\xb5'], ['०', b'\xe0\xa5\xa6'], ['੦', b'\xe0\xa9\xa6'], ['૦', b'\xe0\xab\xa6'], ['௦', b'\xe0\xaf\xa6'], ['ం', b'\xe0\xb0\x82'], ['౦', b'\xe0\xb1\xa6'], ['ಂ', b'\xe0\xb2\x82'], ['೦', b'\xe0\xb3\xa6'], ['ം', b'\xe0\xb4\x82'], ['ഠ', b'\xe0\xb4\xa0'], ['൦', b'\xe0\xb5\xa6'], ['ං', b'\xe0\xb6\x82'], ['๐', b'\xe0\xb9\x90'], ['໐', b'\xe0\xbb\x90'], ['ဝ', b'\xe1\x80\x9d'], ['၀', b'\xe1\x81\x80'], ['ჿ', b'\xe1\x83\xbf'], ['ᴏ', b'\xe1\xb4\x8f'], ['ᴑ', b'\xe1\xb4\x91'], ['ℴ', b'\xe2\x84\xb4'], ['ⲟ', b'\xe2\xb2\x9f'], ['ꬽ', b'\xea\xac\xbd'], ['𐐬', b'\xf0\x90\x90\xac'], ['𐓪', b'\xf0\x90\x93\xaa'], ['𑣈', b'\xf0\x91\xa3\x88'], ['𑣗', b'\xf0\x91\xa3\x97'], ['𝐨', b'\xf0\x9d\x90\xa8'], ['𝑜', b'\xf0\x9d\x91\x9c'], ['𝒐', b'\xf0\x9d\x92\x90'], ['𝓸', b'\xf0\x9d\x93\xb8'], ['𝔬', b'\xf0\x9d\x94\xac'], ['𝕠', b'\xf0\x9d\x95\xa0'], ['𝖔', b'\xf0\x9d\x96\x94'], ['𝗈', b'\xf0\x9d\x97\x88'], ['𝗼', b'\xf0\x9d\x97\xbc'], ['𝘰', b'\xf0\x9d\x98\xb0'], ['𝙤', b'\xf0\x9d\x99\xa4'], ['𝚘', b'\xf0\x9d\x9a\x98'], ['𝛐', b'\xf0\x9d\x9b\x90'], ['𝛔', b'\xf0\x9d\x9b\x94'], ['𝜊', b'\xf0\x9d\x9c\x8a'], ['𝜎', b'\xf0\x9d\x9c\x8e'], ['𝝄', b'\xf0\x9d\x9d\x84'], ['𝝈', b'\xf0\x9d\x9d\x88'], ['𝝾', b'\xf0\x9d\x9d\xbe'], ['𝞂', b'\xf0\x9d\x9e\x82'], ['𝞸', b'\xf0\x9d\x9e\xb8'], ['𝞼', b'\xf0\x9d\x9e\xbc'], ['𞸤', b'\xf0\x9e\xb8\xa4'], ['𞹤', b'\xf0\x9e\xb9\xa4'], ['𞺄', b'\xf0\x9e\xba\x84'], ['ﮦ', b'\xef\xae\xa6'], ['ﮧ', b'\xef\xae\xa7'], ['ﮨ', b'\xef\xae\xa8'], ['ﮩ', b'\xef\xae\xa9'], ['ﮪ', b'\xef\xae\xaa'], ['ﮫ', b'\xef\xae\xab'], ['ﮬ', b'\xef\xae\xac'], ['ﮭ', b'\xef\xae\xad'], ['ﻩ', b'\xef\xbb\xa9'], ['ﻪ', b'\xef\xbb\xaa'], ['ﻫ', b'\xef\xbb\xab'], ['ﻬ', b'\xef\xbb\xac'], ['ｏ', b'\xef\xbd\x8f']],
    [ ['ρ', b'\xcf\x81'], ['ϱ', b'\xcf\xb1'], ['р', b'\xd1\x80'], ['⍴', b'\xe2\x8d\xb4'], ['ⲣ', b'\xe2\xb2\xa3'], ['𝐩', b'\xf0\x9d\x90\xa9'], ['𝑝', b'\xf0\x9d\x91\x9d'], ['𝒑', b'\xf0\x9d\x92\x91'], ['𝓅', b'\xf0\x9d\x93\x85'], ['𝓹', b'\xf0\x9d\x93\xb9'], ['𝔭', b'\xf0\x9d\x94\xad'], ['𝕡', b'\xf0\x9d\x95\xa1'], ['𝖕', b'\xf0\x9d\x96\x95'], ['𝗉', b'\xf0\x9d\x97\x89'], ['𝗽', b'\xf0\x9d\x97\xbd'], ['𝘱', b'\xf0\x9d\x98\xb1'], ['𝙥', b'\xf0\x9d\x99\xa5'], ['𝚙', b'\xf0\x9d\x9a\x99'], ['𝛒', b'\xf0\x9d\x9b\x92'], ['𝛠', b'\xf0\x9d\x9b\xa0'], ['𝜌', b'\xf0\x9d\x9c\x8c'], ['𝜚', b'\xf0\x9d\x9c\x9a'], ['𝝆', b'\xf0\x9d\x9d\x86'], ['𝝔', b'\xf0\x9d\x9d\x94'], ['𝞀', b'\xf0\x9d\x9e\x80'], ['𝞎', b'\xf0\x9d\x9e\x8e'], ['𝞺', b'\xf0\x9d\x9e\xba'], ['𝟈', b'\xf0\x9d\x9f\x88'], ['ｐ', b'\xef\xbd\x90']],
    [ ['ԛ', b'\xd4\x9b'], ['գ', b'\xd5\xa3'], ['զ', b'\xd5\xa6'], ['𝐪', b'\xf0\x9d\x90\xaa'], ['𝑞', b'\xf0\x9d\x91\x9e'], ['𝒒', b'\xf0\x9d\x92\x92'], ['𝓆', b'\xf0\x9d\x93\x86'], ['𝓺', b'\xf0\x9d\x93\xba'], ['𝔮', b'\xf0\x9d\x94\xae'], ['𝕢', b'\xf0\x9d\x95\xa2'], ['𝖖', b'\xf0\x9d\x96\x96'], ['𝗊', b'\xf0\x9d\x97\x8a'], ['𝗾', b'\xf0\x9d\x97\xbe'], ['𝘲', b'\xf0\x9d\x98\xb2'], ['𝙦', b'\xf0\x9d\x99\xa6'], ['𝚚', b'\xf0\x9d\x9a\x9a']],
    [ ['г', b'\xd0\xb3'], ['ᴦ', b'\xe1\xb4\xa6'], ['ⲅ', b'\xe2\xb2\x85'], ['ꭇ', b'\xea\xad\x87'], ['ꭈ', b'\xea\xad\x88'], ['ꮁ', b'\xea\xae\x81'], ['𝐫', b'\xf0\x9d\x90\xab'], ['𝑟', b'\xf0\x9d\x91\x9f'], ['𝒓', b'\xf0\x9d\x92\x93'], ['𝓇', b'\xf0\x9d\x93\x87'], ['𝓻', b'\xf0\x9d\x93\xbb'], ['𝔯', b'\xf0\x9d\x94\xaf'], ['𝕣', b'\xf0\x9d\x95\xa3'], ['𝖗', b'\xf0\x9d\x96\x97'], ['𝗋', b'\xf0\x9d\x97\x8b'], ['𝗿', b'\xf0\x9d\x97\xbf'], ['𝘳', b'\xf0\x9d\x98\xb3'], ['𝙧', b'\xf0\x9d\x99\xa7'], ['𝚛', b'\xf0\x9d\x9a\x9b']],
    [ ['ƽ', b'\xc6\xbd'], ['ѕ', b'\xd1\x95'], ['ꜱ', b'\xea\x9c\xb1'], ['ꮪ', b'\xea\xae\xaa'], ['𐑈', b'\xf0\x90\x91\x88'], ['𑣁', b'\xf0\x91\xa3\x81'], ['𝐬', b'\xf0\x9d\x90\xac'], ['𝑠', b'\xf0\x9d\x91\xa0'], ['𝒔', b'\xf0\x9d\x92\x94'], ['𝓈', b'\xf0\x9d\x93\x88'], ['𝓼', b'\xf0\x9d\x93\xbc'], ['𝔰', b'\xf0\x9d\x94\xb0'], ['𝕤', b'\xf0\x9d\x95\xa4'], ['𝖘', b'\xf0\x9d\x96\x98'], ['𝗌', b'\xf0\x9d\x97\x8c'], ['𝘀', b'\xf0\x9d\x98\x80'], ['𝘴', b'\xf0\x9d\x98\xb4'], ['𝙨', b'\xf0\x9d\x99\xa8'], ['𝚜', b'\xf0\x9d\x9a\x9c'], ['ｓ', b'\xef\xbd\x93']],
    [ ['𝐭', b'\xf0\x9d\x90\xad'], ['𝑡', b'\xf0\x9d\x91\xa1'], ['𝒕', b'\xf0\x9d\x92\x95'], ['𝓉', b'\xf0\x9d\x93\x89'], ['𝓽', b'\xf0\x9d\x93\xbd'], ['𝔱', b'\xf0\x9d\x94\xb1'], ['𝕥', b'\xf0\x9d\x95\xa5'], ['𝖙', b'\xf0\x9d\x96\x99'], ['𝗍', b'\xf0\x9d\x97\x8d'], ['𝘁', b'\xf0\x9d\x98\x81'], ['𝘵', b'\xf0\x9d\x98\xb5'], ['𝙩', b'\xf0\x9d\x99\xa9'], ['𝚝', b'\xf0\x9d\x9a\x9d']],
    [ ['ʋ', b'\xca\x8b'], ['υ', b'\xcf\x85'], ['ս', b'\xd5\xbd'], ['ᴜ', b'\xe1\xb4\x9c'], ['ꞟ', b'\xea\x9e\x9f'], ['ꭎ', b'\xea\xad\x8e'], ['ꭒ', b'\xea\xad\x92'], ['𐓶', b'\xf0\x90\x93\xb6'], ['𑣘', b'\xf0\x91\xa3\x98'], ['𝐮', b'\xf0\x9d\x90\xae'], ['𝑢', b'\xf0\x9d\x91\xa2'], ['𝒖', b'\xf0\x9d\x92\x96'], ['𝓊', b'\xf0\x9d\x93\x8a'], ['𝓾', b'\xf0\x9d\x93\xbe'], ['𝔲', b'\xf0\x9d\x94\xb2'], ['𝕦', b'\xf0\x9d\x95\xa6'], ['𝖚', b'\xf0\x9d\x96\x9a'], ['𝗎', b'\xf0\x9d\x97\x8e'], ['𝘂', b'\xf0\x9d\x98\x82'], ['𝘶', b'\xf0\x9d\x98\xb6'], ['𝙪', b'\xf0\x9d\x99\xaa'], ['𝚞', b'\xf0\x9d\x9a\x9e'], ['𝛖', b'\xf0\x9d\x9b\x96'], ['𝜐', b'\xf0\x9d\x9c\x90'], ['𝝊', b'\xf0\x9d\x9d\x8a'], ['𝞄', b'\xf0\x9d\x9e\x84'], ['𝞾', b'\xf0\x9d\x9e\xbe']],
    [ ['ν', b'\xce\xbd'], ['ѵ', b'\xd1\xb5'], ['ט', b'\xd7\x98'], ['ᴠ', b'\xe1\xb4\xa0'], ['ⅴ', b'\xe2\x85\xb4'], ['∨', b'\xe2\x88\xa8'], ['⋁', b'\xe2\x8b\x81'], ['ꮩ', b'\xea\xae\xa9'], ['𑜆', b'\xf0\x91\x9c\x86'], ['𑣀', b'\xf0\x91\xa3\x80'], ['𝐯', b'\xf0\x9d\x90\xaf'], ['𝑣', b'\xf0\x9d\x91\xa3'], ['𝒗', b'\xf0\x9d\x92\x97'], ['𝓋', b'\xf0\x9d\x93\x8b'], ['𝓿', b'\xf0\x9d\x93\xbf'], ['𝔳', b'\xf0\x9d\x94\xb3'], ['𝕧', b'\xf0\x9d\x95\xa7'], ['𝖛', b'\xf0\x9d\x96\x9b'], ['𝗏', b'\xf0\x9d\x97\x8f'], ['𝘃', b'\xf0\x9d\x98\x83'], ['𝘷', b'\xf0\x9d\x98\xb7'], ['𝙫', b'\xf0\x9d\x99\xab'], ['𝚟', b'\xf0\x9d\x9a\x9f'], ['𝛎', b'\xf0\x9d\x9b\x8e'], ['𝜈', b'\xf0\x9d\x9c\x88'], ['𝝂', b'\xf0\x9d\x9d\x82'], ['𝝼', b'\xf0\x9d\x9d\xbc'], ['𝞶', b'\xf0\x9d\x9e\xb6'], ['ｖ', b'\xef\xbd\x96']],
    [ ['ɯ', b'\xc9\xaf'], ['ѡ', b'\xd1\xa1'], ['ԝ', b'\xd4\x9d'], ['ա', b'\xd5\xa1'], ['ᴡ', b'\xe1\xb4\xa1'], ['ꮃ', b'\xea\xae\x83'], ['𑜊', b'\xf0\x91\x9c\x8a'], ['𑜎', b'\xf0\x91\x9c\x8e'], ['𑜏', b'\xf0\x91\x9c\x8f'], ['𝐰', b'\xf0\x9d\x90\xb0'], ['𝑤', b'\xf0\x9d\x91\xa4'], ['𝒘', b'\xf0\x9d\x92\x98'], ['𝓌', b'\xf0\x9d\x93\x8c'], ['𝔀', b'\xf0\x9d\x94\x80'], ['𝔴', b'\xf0\x9d\x94\xb4'], ['𝕨', b'\xf0\x9d\x95\xa8'], ['𝖜', b'\xf0\x9d\x96\x9c'], ['𝗐', b'\xf0\x9d\x97\x90'], ['𝘄', b'\xf0\x9d\x98\x84'], ['𝘸', b'\xf0\x9d\x98\xb8'], ['𝙬', b'\xf0\x9d\x99\xac'], ['𝚠', b'\xf0\x9d\x9a\xa0']],
    [ ['×', b'\xc3\x97'], ['х', b'\xd1\x85'], ['ᕁ', b'\xe1\x95\x81'], ['ᕽ', b'\xe1\x95\xbd'], ['᙮', b'\xe1\x99\xae'], ['ⅹ', b'\xe2\x85\xb9'], ['⤫', b'\xe2\xa4\xab'], ['⤬', b'\xe2\xa4\xac'], ['⨯', b'\xe2\xa8\xaf'], ['𝐱', b'\xf0\x9d\x90\xb1'], ['𝑥', b'\xf0\x9d\x91\xa5'], ['𝒙', b'\xf0\x9d\x92\x99'], ['𝓍', b'\xf0\x9d\x93\x8d'], ['𝔁', b'\xf0\x9d\x94\x81'], ['𝔵', b'\xf0\x9d\x94\xb5'], ['𝕩', b'\xf0\x9d\x95\xa9'], ['𝖝', b'\xf0\x9d\x96\x9d'], ['𝗑', b'\xf0\x9d\x97\x91'], ['𝘅', b'\xf0\x9d\x98\x85'], ['𝘹', b'\xf0\x9d\x98\xb9'], ['𝙭', b'\xf0\x9d\x99\xad'], ['𝚡', b'\xf0\x9d\x9a\xa1'], ['ｘ', b'\xef\xbd\x98']],
    [ ['ɣ', b'\xc9\xa3'], ['ʏ', b'\xca\x8f'], ['γ', b'\xce\xb3'], ['у', b'\xd1\x83'], ['ү', b'\xd2\xaf'], ['ყ', b'\xe1\x83\xa7'], ['ᶌ', b'\xe1\xb6\x8c'], ['ỿ', b'\xe1\xbb\xbf'], ['ℽ', b'\xe2\x84\xbd'], ['ꭚ', b'\xea\xad\x9a'], ['𑣜', b'\xf0\x91\xa3\x9c'], ['𝐲', b'\xf0\x9d\x90\xb2'], ['𝑦', b'\xf0\x9d\x91\xa6'], ['𝒚', b'\xf0\x9d\x92\x9a'], ['𝓎', b'\xf0\x9d\x93\x8e'], ['𝔂', b'\xf0\x9d\x94\x82'], ['𝔶', b'\xf0\x9d\x94\xb6'], ['𝕪', b'\xf0\x9d\x95\xaa'], ['𝖞', b'\xf0\x9d\x96\x9e'], ['𝗒', b'\xf0\x9d\x97\x92'], ['𝘆', b'\xf0\x9d\x98\x86'], ['𝘺', b'\xf0\x9d\x98\xba'], ['𝙮', b'\xf0\x9d\x99\xae'], ['𝚢', b'\xf0\x9d\x9a\xa2'], ['𝛄', b'\xf0\x9d\x9b\x84'], ['𝛾', b'\xf0\x9d\x9b\xbe'], ['𝜸', b'\xf0\x9d\x9c\xb8'], ['𝝲', b'\xf0\x9d\x9d\xb2'], ['𝞬', b'\xf0\x9d\x9e\xac'], ['ｙ', b'\xef\xbd\x99']],
    [ ['ᴢ', b'\xe1\xb4\xa2'], ['ꮓ', b'\xea\xae\x93'], ['𑣄', b'\xf0\x91\xa3\x84'], ['𝐳', b'\xf0\x9d\x90\xb3'], ['𝑧', b'\xf0\x9d\x91\xa7'], ['𝒛', b'\xf0\x9d\x92\x9b'], ['𝓏', b'\xf0\x9d\x93\x8f'], ['𝔃', b'\xf0\x9d\x94\x83'], ['𝔷', b'\xf0\x9d\x94\xb7'], ['𝕫', b'\xf0\x9d\x95\xab'], ['𝖟', b'\xf0\x9d\x96\x9f'], ['𝗓', b'\xf0\x9d\x97\x93'], ['𝘇', b'\xf0\x9d\x98\x87'], ['𝘻', b'\xf0\x9d\x98\xbb'], ['𝙯', b'\xf0\x9d\x99\xaf'], ['𝚣', b'\xf0\x9d\x9a\xa3']],
    [ ['Α', b'\xce\x91'], ['А', b'\xd0\x90'], ['Ꭺ', b'\xe1\x8e\xaa'], ['ᗅ', b'\xe1\x97\x85'], ['ꓮ', b'\xea\x93\xae'], ['𐊠', b'\xf0\x90\x8a\xa0'], ['𖽀', b'\xf0\x96\xbd\x80'], ['𝐀', b'\xf0\x9d\x90\x80'], ['𝐴', b'\xf0\x9d\x90\xb4'], ['𝑨', b'\xf0\x9d\x91\xa8'], ['𝒜', b'\xf0\x9d\x92\x9c'], ['𝓐', b'\xf0\x9d\x93\x90'], ['𝔄', b'\xf0\x9d\x94\x84'], ['𝔸', b'\xf0\x9d\x94\xb8'], ['𝕬', b'\xf0\x9d\x95\xac'], ['𝖠', b'\xf0\x9d\x96\xa0'], ['𝗔', b'\xf0\x9d\x97\x94'], ['𝘈', b'\xf0\x9d\x98\x88'], ['𝘼', b'\xf0\x9d\x98\xbc'], ['𝙰', b'\xf0\x9d\x99\xb0'], ['𝚨', b'\xf0\x9d\x9a\xa8'], ['𝛢', b'\xf0\x9d\x9b\xa2'], ['𝜜', b'\xf0\x9d\x9c\x9c'], ['𝝖', b'\xf0\x9d\x9d\x96'], ['𝞐', b'\xf0\x9d\x9e\x90'], ['Ａ', b'\xef\xbc\xa1']],
    [ ['Β', b'\xce\x92'], ['В', b'\xd0\x92'], ['Ᏼ', b'\xe1\x8f\xb4'], ['ᗷ', b'\xe1\x97\xb7'], ['ℬ', b'\xe2\x84\xac'], ['ꓐ', b'\xea\x93\x90'], ['Ꞵ', b'\xea\x9e\xb4'], ['𐊂', b'\xf0\x90\x8a\x82'], ['𐊡', b'\xf0\x90\x8a\xa1'], ['𐌁', b'\xf0\x90\x8c\x81'], ['𝐁', b'\xf0\x9d\x90\x81'], ['𝐵', b'\xf0\x9d\x90\xb5'], ['𝑩', b'\xf0\x9d\x91\xa9'], ['𝓑', b'\xf0\x9d\x93\x91'], ['𝔅', b'\xf0\x9d\x94\x85'], ['𝔹', b'\xf0\x9d\x94\xb9'], ['𝕭', b'\xf0\x9d\x95\xad'], ['𝖡', b'\xf0\x9d\x96\xa1'], ['𝗕', b'\xf0\x9d\x97\x95'], ['𝘉', b'\xf0\x9d\x98\x89'], ['𝘽', b'\xf0\x9d\x98\xbd'], ['𝙱', b'\xf0\x9d\x99\xb1'], ['𝚩', b'\xf0\x9d\x9a\xa9'], ['𝛣', b'\xf0\x9d\x9b\xa3'], ['𝜝', b'\xf0\x9d\x9c\x9d'], ['𝝗', b'\xf0\x9d\x9d\x97'], ['𝞑', b'\xf0\x9d\x9e\x91'], ['Ｂ', b'\xef\xbc\xa2']],
    [ ['Ϲ', b'\xcf\xb9'], ['С', b'\xd0\xa1'], ['Ꮯ', b'\xe1\x8f\x9f'], ['ℂ', b'\xe2\x84\x82'], ['ℭ', b'\xe2\x84\xad'], ['Ⅽ', b'\xe2\x85\xad'], ['Ⲥ', b'\xe2\xb2\xa4'], ['ꓚ', b'\xea\x93\x9a'], ['𐊢', b'\xf0\x90\x8a\xa2'], ['𐌂', b'\xf0\x90\x8c\x82'], ['𐐕', b'\xf0\x90\x90\x95'], ['𐔜', b'\xf0\x90\x94\x9c'], ['𑣩', b'\xf0\x91\xa3\xa9'], ['𑣲', b'\xf0\x91\xa3\xb2'], ['𝐂', b'\xf0\x9d\x90\x82'], ['𝐶', b'\xf0\x9d\x90\xb6'], ['𝑪', b'\xf0\x9d\x91\xaa'], ['𝒞', b'\xf0\x9d\x92\x9e'], ['𝓒', b'\xf0\x9d\x93\x92'], ['𝕮', b'\xf0\x9d\x95\xae'], ['𝖢', b'\xf0\x9d\x96\xa2'], ['𝗖', b'\xf0\x9d\x97\x96'], ['𝘊', b'\xf0\x9d\x98\x8a'], ['𝘾', b'\xf0\x9d\x98\xbe'], ['𝙲', b'\xf0\x9d\x99\xb2'], ['🝌', b'\xf0\x9f\x9d\x8c'], ['Ｃ', b'\xef\xbc\xa3']],
    [ ['Ꭰ', b'\xe1\x8e\xa0'], ['ᗞ', b'\xe1\x97\x9e'], ['ᗪ', b'\xe1\x97\xaa'], ['ⅅ', b'\xe2\x85\x85'], ['Ⅾ', b'\xe2\x85\xae'], ['ꓓ', b'\xea\x93\x93'], ['𝐃', b'\xf0\x9d\x90\x83'], ['𝐷', b'\xf0\x9d\x90\xb7'], ['𝑫', b'\xf0\x9d\x91\xab'], ['𝒟', b'\xf0\x9d\x92\x9f'], ['𝓓', b'\xf0\x9d\x93\x93'], ['𝔇', b'\xf0\x9d\x94\x87'], ['𝔻', b'\xf0\x9d\x94\xbb'], ['𝕯', b'\xf0\x9d\x95\xaf'], ['𝖣', b'\xf0\x9d\x96\xa3'], ['𝗗', b'\xf0\x9d\x97\x97'], ['𝘋', b'\xf0\x9d\x98\x8b'], ['𝘿', b'\xf0\x9d\x98\xbf'], ['𝙳', b'\xf0\x9d\x99\xb3']],
    [ ['Ε', b'\xce\x95'], ['Е', b'\xd0\x95'], ['Ꭼ', b'\xe1\x8e\xac'], ['ℰ', b'\xe2\x84\xb0'], ['⋿', b'\xe2\x8b\xbf'], ['ⴹ', b'\xe2\xb4\xb9'], ['ꓰ', b'\xea\x93\xb0'], ['𐊆', b'\xf0\x90\x8a\x86'], ['𑢦', b'\xf0\x91\xa2\xa6'], ['𑢮', b'\xf0\x91\xa2\xae'], ['𝐄', b'\xf0\x9d\x90\x84'], ['𝐸', b'\xf0\x9d\x90\xb8'], ['𝑬', b'\xf0\x9d\x91\xac'], ['𝓔', b'\xf0\x9d\x93\x94'], ['𝔈', b'\xf0\x9d\x94\x88'], ['𝔼', b'\xf0\x9d\x94\xbc'], ['𝕰', b'\xf0\x9d\x95\xb0'], ['𝖤', b'\xf0\x9d\x96\xa4'], ['𝗘', b'\xf0\x9d\x97\x98'], ['𝘌', b'\xf0\x9d\x98\x8c'], ['𝙀', b'\xf0\x9d\x99\x80'], ['𝙴', b'\xf0\x9d\x99\xb4'], ['𝚬', b'\xf0\x9d\x9a\xac'], ['𝛦', b'\xf0\x9d\x9b\xa6'], ['𝜠', b'\xf0\x9d\x9c\xa0'], ['𝝚', b'\xf0\x9d\x9d\x9a'], ['𝞔', b'\xf0\x9d\x9e\x94'], ['Ｅ', b'\xef\xbc\xa5']],
    [ ['Ϝ', b'\xcf\x9c'], ['ᖴ', b'\xe1\x96\xb4'], ['ℱ', b'\xe2\x84\xb1'], ['ꓝ', b'\xea\x93\x9d'], ['Ꞙ', b'\xea\x9e\x98'], ['𐊇', b'\xf0\x90\x8a\x87'], ['𐊥', b'\xf0\x90\x8a\xa5'], ['𐔥', b'\xf0\x90\x94\xa5'], ['𑢢', b'\xf0\x91\xa2\xa2'], ['𑣂', b'\xf0\x91\xa3\x82'], ['𝈓', b'\xf0\x9d\x88\x93'], ['𝐅', b'\xf0\x9d\x90\x85'], ['𝐹', b'\xf0\x9d\x90\xb9'], ['𝑭', b'\xf0\x9d\x91\xad'], ['𝓕', b'\xf0\x9d\x93\x95'], ['𝔉', b'\xf0\x9d\x94\x89'], ['𝔽', b'\xf0\x9d\x94\xbd'], ['𝕱', b'\xf0\x9d\x95\xb1'], ['𝖥', b'\xf0\x9d\x96\xa5'], ['𝗙', b'\xf0\x9d\x97\x99'], ['𝘍', b'\xf0\x9d\x98\x8d'], ['𝙁', b'\xf0\x9d\x99\x81'], ['𝙵', b'\xf0\x9d\x99\xb5'], ['𝟊', b'\xf0\x9d\x9f\x8a']],
    [ ['Ԍ', b'\xd4\x8c'], ['Ꮐ', b'\xe1\x8f\x80'], ['Ᏻ', b'\xe1\x8f\xb3'], ['ꓖ', b'\xea\x93\x96'], ['𝐆', b'\xf0\x9d\x90\x86'], ['𝐺', b'\xf0\x9d\x90\xba'], ['𝑮', b'\xf0\x9d\x91\xae'], ['𝒢', b'\xf0\x9d\x92\xa2'], ['𝓖', b'\xf0\x9d\x93\x96'], ['𝔊', b'\xf0\x9d\x94\x8a'], ['𝔾', b'\xf0\x9d\x94\xbe'], ['𝕲', b'\xf0\x9d\x95\xb2'], ['𝖦', b'\xf0\x9d\x96\xa6'], ['𝗚', b'\xf0\x9d\x97\x9a'], ['𝘎', b'\xf0\x9d\x98\x8e'], ['𝙂', b'\xf0\x9d\x99\x82'], ['𝙶', b'\xf0\x9d\x99\xb6']],
    [ ['Η', b'\xce\x97'], ['Н', b'\xd0\x9d'], ['Ꮋ', b'\xe1\x8e\xbb'], ['ᕼ', b'\xe1\x95\xbc'], ['ℋ', b'\xe2\x84\x8b'], ['ℌ', b'\xe2\x84\x8c'], ['ℍ', b'\xe2\x84\x8d'], ['Ⲏ', b'\xe2\xb2\x8e'], ['ꓧ', b'\xea\x93\xa7'], ['𐋏', b'\xf0\x90\x8b\x8f'], ['𝐇', b'\xf0\x9d\x90\x87'], ['𝐻', b'\xf0\x9d\x90\xbb'], ['𝑯', b'\xf0\x9d\x91\xaf'], ['𝓗', b'\xf0\x9d\x93\x97'], ['𝕳', b'\xf0\x9d\x95\xb3'], ['𝖧', b'\xf0\x9d\x96\xa7'], ['𝗛', b'\xf0\x9d\x97\x9b'], ['𝘏', b'\xf0\x9d\x98\x8f'], ['𝙃', b'\xf0\x9d\x99\x83'], ['𝙷', b'\xf0\x9d\x99\xb7'], ['𝚮', b'\xf0\x9d\x9a\xae'], ['𝛨', b'\xf0\x9d\x9b\xa8'], ['𝜢', b'\xf0\x9d\x9c\xa2'], ['𝝜', b'\xf0\x9d\x9d\x9c'], ['𝞖', b'\xf0\x9d\x9e\x96'], ['Ｈ', b'\xef\xbc\xa8']],
    [ ['Ɩ', b'\xc6\x96'], ['ǀ', b'\xc7\x80'], ['Ι', b'\xce\x99'], ['І', b'\xd0\x86'], ['Ӏ', b'\xd3\x80'], ['׀', b'\xd7\x80'], ['ו', b'\xd7\x95'], ['ן', b'\xd7\x9f'], ['ا', b'\xd8\xa7'], ['١', b'\xd9\xa1'], ['۱', b'\xdb\xb1'], ['ߊ', b'\xdf\x8a'], ['ᛁ', b'\xe1\x9b\x81'], ['ℐ', b'\xe2\x84\x90'], ['ℑ', b'\xe2\x84\x91'], ['ℓ', b'\xe2\x84\x93'], ['Ⅰ', b'\xe2\x85\xa0'], ['ⅼ', b'\xe2\x85\xbc'], ['∣', b'\xe2\x88\xa3'], ['⏽', b'\xe2\x8f\xbd'], ['Ⲓ', b'\xe2\xb2\x92'], ['ⵏ', b'\xe2\xb5\x8f'], ['ꓲ', b'\xea\x93\xb2'], ['𐊊', b'\xf0\x90\x8a\x8a'], ['𐌉', b'\xf0\x90\x8c\x89'], ['𐌠', b'\xf0\x90\x8c\xa0'], ['𖼨', b'\xf0\x96\xbc\xa8'], ['𝐈', b'\xf0\x9d\x90\x88'], ['𝐥', b'\xf0\x9d\x90\xa5'], ['𝐼', b'\xf0\x9d\x90\xbc'], ['𝑙', b'\xf0\x9d\x91\x99'], ['𝑰', b'\xf0\x9d\x91\xb0'], ['𝒍', b'\xf0\x9d\x92\x8d'], ['𝓁', b'\xf0\x9d\x93\x81'], ['𝓘', b'\xf0\x9d\x93\x98'], ['𝓵', b'\xf0\x9d\x93\xb5'], ['𝔩', b'\xf0\x9d\x94\xa9'], ['𝕀', b'\xf0\x9d\x95\x80'], ['𝕝', b'\xf0\x9d\x95\x9d'], ['𝕴', b'\xf0\x9d\x95\xb4'], ['𝖑', b'\xf0\x9d\x96\x91'], ['𝖨', b'\xf0\x9d\x96\xa8'], ['𝗅', b'\xf0\x9d\x97\x85'], ['𝗜', b'\xf0\x9d\x97\x9c'], ['𝗹', b'\xf0\x9d\x97\xb9'], ['𝘐', b'\xf0\x9d\x98\x90'], ['𝘭', b'\xf0\x9d\x98\xad'], ['𝙄', b'\xf0\x9d\x99\x84'], ['𝙡', b'\xf0\x9d\x99\xa1'], ['𝙸', b'\xf0\x9d\x99\xb8'], ['𝚕', b'\xf0\x9d\x9a\x95'], ['𝚰', b'\xf0\x9d\x9a\xb0'], ['𝛪', b'\xf0\x9d\x9b\xaa'], ['𝜤', b'\xf0\x9d\x9c\xa4'], ['𝝞', b'\xf0\x9d\x9d\x9e'], ['𝞘', b'\xf0\x9d\x9e\x98'], ['𝟏', b'\xf0\x9d\x9f\x8f'], ['𝟙', b'\xf0\x9d\x9f\x99'], ['𝟣', b'\xf0\x9d\x9f\xa3'], ['𝟭', b'\xf0\x9d\x9f\xad'], ['𝟷', b'\xf0\x9d\x9f\xb7'], ['𞣇', b'\xf0\x9e\xa3\x87'], ['𞸀', b'\xf0\x9e\xb8\x80'], ['𞺀', b'\xf0\x9e\xba\x80'], ['🯱', b'\xf0\x9f\xaf\xb1'], ['ﺍ', b'\xef\xba\x8d'], ['ﺎ', b'\xef\xba\x8e'], ['Ｉ', b'\xef\xbc\xa9'], ['ｌ', b'\xef\xbd\x8c'], ['￨', b'\xef\xbf\xa8']],
    [ ['Ϳ', b'\xcd\xbf'], ['Ј', b'\xd0\x88'], ['Ꭻ', b'\xe1\x8e\xab'], ['ᒍ', b'\xe1\x92\x8d'], ['ꓙ', b'\xea\x93\x99'], ['Ʝ', b'\xea\x9e\xb2'], ['𝐉', b'\xf0\x9d\x90\x89'], ['𝐽', b'\xf0\x9d\x90\xbd'], ['𝑱', b'\xf0\x9d\x91\xb1'], ['𝒥', b'\xf0\x9d\x92\xa5'], ['𝓙', b'\xf0\x9d\x93\x99'], ['𝔍', b'\xf0\x9d\x94\x8d'], ['𝕁', b'\xf0\x9d\x95\x81'], ['𝕵', b'\xf0\x9d\x95\xb5'], ['𝖩', b'\xf0\x9d\x96\xa9'], ['𝗝', b'\xf0\x9d\x97\x9d'], ['𝘑', b'\xf0\x9d\x98\x91'], ['𝙅', b'\xf0\x9d\x99\x85'], ['𝙹', b'\xf0\x9d\x99\xb9'], ['Ｊ', b'\xef\xbc\xaa']],
    [ ['Κ', b'\xce\x9a'], ['К', b'\xd0\x9a'], ['Ꮶ', b'\xe1\x8f\xa6'], ['ᛕ', b'\xe1\x9b\x95'], ['K', b'\xe2\x84\xaa'], ['Ⲕ', b'\xe2\xb2\x94'], ['ꓗ', b'\xea\x93\x97'], ['𐔘', b'\xf0\x90\x94\x98'], ['𝐊', b'\xf0\x9d\x90\x8a'], ['𝐾', b'\xf0\x9d\x90\xbe'], ['𝑲', b'\xf0\x9d\x91\xb2'], ['𝒦', b'\xf0\x9d\x92\xa6'], ['𝓚', b'\xf0\x9d\x93\x9a'], ['𝔎', b'\xf0\x9d\x94\x8e'], ['𝕂', b'\xf0\x9d\x95\x82'], ['𝕶', b'\xf0\x9d\x95\xb6'], ['𝖪', b'\xf0\x9d\x96\xaa'], ['𝗞', b'\xf0\x9d\x97\x9e'], ['𝘒', b'\xf0\x9d\x98\x92'], ['𝙆', b'\xf0\x9d\x99\x86'], ['𝙺', b'\xf0\x9d\x99\xba'], ['𝚱', b'\xf0\x9d\x9a\xb1'], ['𝛫', b'\xf0\x9d\x9b\xab'], ['𝜥', b'\xf0\x9d\x9c\xa5'], ['𝝟', b'\xf0\x9d\x9d\x9f'], ['𝞙', b'\xf0\x9d\x9e\x99'], ['Ｋ', b'\xef\xbc\xab']],
    [ ['Ꮮ', b'\xe1\x8f\x9e'], ['ᒪ', b'\xe1\x92\xaa'], ['ℒ', b'\xe2\x84\x92'], ['Ⅼ', b'\xe2\x85\xac'], ['Ⳑ', b'\xe2\xb3\x90'], ['ꓡ', b'\xea\x93\xa1'], ['𐐛', b'\xf0\x90\x90\x9b'], ['𐔦', b'\xf0\x90\x94\xa6'], ['𑢣', b'\xf0\x91\xa2\xa3'], ['𑢲', b'\xf0\x91\xa2\xb2'], ['𖼖', b'\xf0\x96\xbc\x96'], ['𝈪', b'\xf0\x9d\x88\xaa'], ['𝐋', b'\xf0\x9d\x90\x8b'], ['𝐿', b'\xf0\x9d\x90\xbf'], ['𝑳', b'\xf0\x9d\x91\xb3'], ['𝓛', b'\xf0\x9d\x93\x9b'], ['𝔏', b'\xf0\x9d\x94\x8f'], ['𝕃', b'\xf0\x9d\x95\x83'], ['𝕷', b'\xf0\x9d\x95\xb7'], ['𝖫', b'\xf0\x9d\x96\xab'], ['𝗟', b'\xf0\x9d\x97\x9f'], ['𝘓', b'\xf0\x9d\x98\x93'], ['𝙇', b'\xf0\x9d\x99\x87'], ['𝙻', b'\xf0\x9d\x99\xbb']],
    [ ['Μ', b'\xce\x9c'], ['Ϻ', b'\xcf\xba'], ['М', b'\xd0\x9c'], ['Ꮇ', b'\xe1\x8e\xb7'], ['ᗰ', b'\xe1\x97\xb0'], ['ᛖ', b'\xe1\x9b\x96'], ['ℳ', b'\xe2\x84\xb3'], ['Ⅿ', b'\xe2\x85\xaf'], ['Ⲙ', b'\xe2\xb2\x98'], ['ꓟ', b'\xea\x93\x9f'], ['𐊰', b'\xf0\x90\x8a\xb0'], ['𐌑', b'\xf0\x90\x8c\x91'], ['𝐌', b'\xf0\x9d\x90\x8c'], ['𝑀', b'\xf0\x9d\x91\x80'], ['𝑴', b'\xf0\x9d\x91\xb4'], ['𝓜', b'\xf0\x9d\x93\x9c'], ['𝔐', b'\xf0\x9d\x94\x90'], ['𝕄', b'\xf0\x9d\x95\x84'], ['𝕸', b'\xf0\x9d\x95\xb8'], ['𝖬', b'\xf0\x9d\x96\xac'], ['𝗠', b'\xf0\x9d\x97\xa0'], ['𝘔', b'\xf0\x9d\x98\x94'], ['𝙈', b'\xf0\x9d\x99\x88'], ['𝙼', b'\xf0\x9d\x99\xbc'], ['𝚳', b'\xf0\x9d\x9a\xb3'], ['𝛭', b'\xf0\x9d\x9b\xad'], ['𝜧', b'\xf0\x9d\x9c\xa7'], ['𝝡', b'\xf0\x9d\x9d\xa1'], ['𝞛', b'\xf0\x9d\x9e\x9b'], ['Ｍ', b'\xef\xbc\xad']],
    [ ['Ν', b'\xce\x9d'], ['ℕ', b'\xe2\x84\x95'], ['Ⲛ', b'\xe2\xb2\x9a'], ['ꓠ', b'\xea\x93\xa0'], ['𐔓', b'\xf0\x90\x94\x93'], ['𝐍', b'\xf0\x9d\x90\x8d'], ['𝑁', b'\xf0\x9d\x91\x81'], ['𝑵', b'\xf0\x9d\x91\xb5'], ['𝒩', b'\xf0\x9d\x92\xa9'], ['𝓝', b'\xf0\x9d\x93\x9d'], ['𝔑', b'\xf0\x9d\x94\x91'], ['𝕹', b'\xf0\x9d\x95\xb9'], ['𝖭', b'\xf0\x9d\x96\xad'], ['𝗡', b'\xf0\x9d\x97\xa1'], ['𝘕', b'\xf0\x9d\x98\x95'], ['𝙉', b'\xf0\x9d\x99\x89'], ['𝙽', b'\xf0\x9d\x99\xbd'], ['𝚴', b'\xf0\x9d\x9a\xb4'], ['𝛮', b'\xf0\x9d\x9b\xae'], ['𝜨', b'\xf0\x9d\x9c\xa8'], ['𝝢', b'\xf0\x9d\x9d\xa2'], ['𝞜', b'\xf0\x9d\x9e\x9c'], ['Ｎ', b'\xef\xbc\xae']],
    [ ['Ο', b'\xce\x9f'], ['О', b'\xd0\x9e'], ['Օ', b'\xd5\x95'], ['߀', b'\xdf\x80'], ['০', b'\xe0\xa7\xa6'], ['ଠ', b'\xe0\xac\xa0'], ['୦', b'\xe0\xad\xa6'], ['ዐ', b'\xe1\x8b\x90'], ['Ⲟ', b'\xe2\xb2\x9e'], ['ⵔ', b'\xe2\xb5\x94'], ['〇', b'\xe3\x80\x87'], ['ꓳ', b'\xea\x93\xb3'], ['𐊒', b'\xf0\x90\x8a\x92'], ['𐊫', b'\xf0\x90\x8a\xab'], ['𐐄', b'\xf0\x90\x90\x84'], ['𐓂', b'\xf0\x90\x93\x82'], ['𐔖', b'\xf0\x90\x94\x96'], ['𑓐', b'\xf0\x91\x93\x90'], ['𑢵', b'\xf0\x91\xa2\xb5'], ['𑣠', b'\xf0\x91\xa3\xa0'], ['𝐎', b'\xf0\x9d\x90\x8e'], ['𝑂', b'\xf0\x9d\x91\x82'], ['𝑶', b'\xf0\x9d\x91\xb6'], ['𝒪', b'\xf0\x9d\x92\xaa'], ['𝓞', b'\xf0\x9d\x93\x9e'], ['𝔒', b'\xf0\x9d\x94\x92'], ['𝕆', b'\xf0\x9d\x95\x86'], ['𝕺', b'\xf0\x9d\x95\xba'], ['𝖮', b'\xf0\x9d\x96\xae'], ['𝗢', b'\xf0\x9d\x97\xa2'], ['𝘖', b'\xf0\x9d\x98\x96'], ['𝙊', b'\xf0\x9d\x99\x8a'], ['𝙾', b'\xf0\x9d\x99\xbe'], ['𝚶', b'\xf0\x9d\x9a\xb6'], ['𝛰', b'\xf0\x9d\x9b\xb0'], ['𝜪', b'\xf0\x9d\x9c\xaa'], ['𝝤', b'\xf0\x9d\x9d\xa4'], ['𝞞', b'\xf0\x9d\x9e\x9e'], ['𝟎', b'\xf0\x9d\x9f\x8e'], ['𝟘', b'\xf0\x9d\x9f\x98'], ['𝟢', b'\xf0\x9d\x9f\xa2'], ['𝟬', b'\xf0\x9d\x9f\xac'], ['𝟶', b'\xf0\x9d\x9f\xb6'], ['🯰', b'\xf0\x9f\xaf\xb0'], ['Ｏ', b'\xef\xbc\xaf']],
    [ ['Ρ', b'\xce\xa1'], ['Р', b'\xd0\xa0'], ['Ꮲ', b'\xe1\x8f\xa2'], ['ᑭ', b'\xe1\x91\xad'], ['ℙ', b'\xe2\x84\x99'], ['Ⲣ', b'\xe2\xb2\xa2'], ['ꓑ', b'\xea\x93\x91'], ['𐊕', b'\xf0\x90\x8a\x95'], ['𝐏', b'\xf0\x9d\x90\x8f'], ['𝑃', b'\xf0\x9d\x91\x83'], ['𝑷', b'\xf0\x9d\x91\xb7'], ['𝒫', b'\xf0\x9d\x92\xab'], ['𝓟', b'\xf0\x9d\x93\x9f'], ['𝔓', b'\xf0\x9d\x94\x93'], ['𝕻', b'\xf0\x9d\x95\xbb'], ['𝖯', b'\xf0\x9d\x96\xaf'], ['𝗣', b'\xf0\x9d\x97\xa3'], ['𝘗', b'\xf0\x9d\x98\x97'], ['𝙋', b'\xf0\x9d\x99\x8b'], ['𝙿', b'\xf0\x9d\x99\xbf'], ['𝚸', b'\xf0\x9d\x9a\xb8'], ['𝛲', b'\xf0\x9d\x9b\xb2'], ['𝜬', b'\xf0\x9d\x9c\xac'], ['𝝦', b'\xf0\x9d\x9d\xa6'], ['𝞠', b'\xf0\x9d\x9e\xa0'], ['Ｐ', b'\xef\xbc\xb0']],
    [ ['ℚ', b'\xe2\x84\x9a'], ['ⵕ', b'\xe2\xb5\x95'], ['𝐐', b'\xf0\x9d\x90\x90'], ['𝑄', b'\xf0\x9d\x91\x84'], ['𝑸', b'\xf0\x9d\x91\xb8'], ['𝒬', b'\xf0\x9d\x92\xac'], ['𝓠', b'\xf0\x9d\x93\xa0'], ['𝔔', b'\xf0\x9d\x94\x94'], ['𝕼', b'\xf0\x9d\x95\xbc'], ['𝖰', b'\xf0\x9d\x96\xb0'], ['𝗤', b'\xf0\x9d\x97\xa4'], ['𝘘', b'\xf0\x9d\x98\x98'], ['𝙌', b'\xf0\x9d\x99\x8c'], ['𝚀', b'\xf0\x9d\x9a\x80']],
    [ ['Ʀ', b'\xc6\xa6'], ['Ꭱ', b'\xe1\x8e\xa1'], ['Ꮢ', b'\xe1\x8f\x92'], ['ᖇ', b'\xe1\x96\x87'], ['ℛ', b'\xe2\x84\x9b'], ['ℜ', b'\xe2\x84\x9c'], ['ℝ', b'\xe2\x84\x9d'], ['ꓣ', b'\xea\x93\xa3'], ['𐒴', b'\xf0\x90\x92\xb4'], ['𖼵', b'\xf0\x96\xbc\xb5'], ['𝈖', b'\xf0\x9d\x88\x96'], ['𝐑', b'\xf0\x9d\x90\x91'], ['𝑅', b'\xf0\x9d\x91\x85'], ['𝑹', b'\xf0\x9d\x91\xb9'], ['𝓡', b'\xf0\x9d\x93\xa1'], ['𝕽', b'\xf0\x9d\x95\xbd'], ['𝖱', b'\xf0\x9d\x96\xb1'], ['𝗥', b'\xf0\x9d\x97\xa5'], ['𝘙', b'\xf0\x9d\x98\x99'], ['𝙍', b'\xf0\x9d\x99\x8d'], ['𝚁', b'\xf0\x9d\x9a\x81']],
    [ ['Ѕ', b'\xd0\x85'], ['Տ', b'\xd5\x8f'], ['Ꮥ', b'\xe1\x8f\x95'], ['Ꮪ', b'\xe1\x8f\x9a'], ['ꓢ', b'\xea\x93\xa2'], ['𐊖', b'\xf0\x90\x8a\x96'], ['𐐠', b'\xf0\x90\x90\xa0'], ['𖼺', b'\xf0\x96\xbc\xba'], ['𝐒', b'\xf0\x9d\x90\x92'], ['𝑆', b'\xf0\x9d\x91\x86'], ['𝑺', b'\xf0\x9d\x91\xba'], ['𝒮', b'\xf0\x9d\x92\xae'], ['𝓢', b'\xf0\x9d\x93\xa2'], ['𝔖', b'\xf0\x9d\x94\x96'], ['𝕊', b'\xf0\x9d\x95\x8a'], ['𝕾', b'\xf0\x9d\x95\xbe'], ['𝖲', b'\xf0\x9d\x96\xb2'], ['𝗦', b'\xf0\x9d\x97\xa6'], ['𝘚', b'\xf0\x9d\x98\x9a'], ['𝙎', b'\xf0\x9d\x99\x8e'], ['𝚂', b'\xf0\x9d\x9a\x82'], ['Ｓ', b'\xef\xbc\xb3']],
    [ ['Τ', b'\xce\xa4'], ['Т', b'\xd0\xa2'], ['Ꭲ', b'\xe1\x8e\xa2'], ['⊤', b'\xe2\x8a\xa4'], ['⟙', b'\xe2\x9f\x99'], ['Ⲧ', b'\xe2\xb2\xa6'], ['ꓔ', b'\xea\x93\x94'], ['𐊗', b'\xf0\x90\x8a\x97'], ['𐊱', b'\xf0\x90\x8a\xb1'], ['𐌕', b'\xf0\x90\x8c\x95'], ['𑢼', b'\xf0\x91\xa2\xbc'], ['𖼊', b'\xf0\x96\xbc\x8a'], ['𝐓', b'\xf0\x9d\x90\x93'], ['𝑇', b'\xf0\x9d\x91\x87'], ['𝑻', b'\xf0\x9d\x91\xbb'], ['𝒯', b'\xf0\x9d\x92\xaf'], ['𝓣', b'\xf0\x9d\x93\xa3'], ['𝔗', b'\xf0\x9d\x94\x97'], ['𝕋', b'\xf0\x9d\x95\x8b'], ['𝕿', b'\xf0\x9d\x95\xbf'], ['𝖳', b'\xf0\x9d\x96\xb3'], ['𝗧', b'\xf0\x9d\x97\xa7'], ['𝘛', b'\xf0\x9d\x98\x9b'], ['𝙏', b'\xf0\x9d\x99\x8f'], ['𝚃', b'\xf0\x9d\x9a\x83'], ['𝚻', b'\xf0\x9d\x9a\xbb'], ['𝛵', b'\xf0\x9d\x9b\xb5'], ['𝜯', b'\xf0\x9d\x9c\xaf'], ['𝝩', b'\xf0\x9d\x9d\xa9'], ['𝞣', b'\xf0\x9d\x9e\xa3'], ['🝨', b'\xf0\x9f\x9d\xa8'], ['Ｔ', b'\xef\xbc\xb4']],
    [ ['Ս', b'\xd5\x8d'], ['ሀ', b'\xe1\x88\x80'], ['ᑌ', b'\xe1\x91\x8c'], ['∪', b'\xe2\x88\xaa'], ['⋃', b'\xe2\x8b\x83'], ['ꓴ', b'\xea\x93\xb4'], ['𐓎', b'\xf0\x90\x93\x8e'], ['𑢸', b'\xf0\x91\xa2\xb8'], ['𖽂', b'\xf0\x96\xbd\x82'], ['𝐔', b'\xf0\x9d\x90\x94'], ['𝑈', b'\xf0\x9d\x91\x88'], ['𝑼', b'\xf0\x9d\x91\xbc'], ['𝒰', b'\xf0\x9d\x92\xb0'], ['𝓤', b'\xf0\x9d\x93\xa4'], ['𝔘', b'\xf0\x9d\x94\x98'], ['𝕌', b'\xf0\x9d\x95\x8c'], ['𝖀', b'\xf0\x9d\x96\x80'], ['𝖴', b'\xf0\x9d\x96\xb4'], ['𝗨', b'\xf0\x9d\x97\xa8'], ['𝘜', b'\xf0\x9d\x98\x9c'], ['𝙐', b'\xf0\x9d\x99\x90'], ['𝚄', b'\xf0\x9d\x9a\x84']],
    [ ['Ѵ', b'\xd1\xb4'], ['٧', b'\xd9\xa7'], ['۷', b'\xdb\xb7'], ['Ꮩ', b'\xe1\x8f\x99'], ['ᐯ', b'\xe1\x90\xaf'], ['Ⅴ', b'\xe2\x85\xa4'], ['ⴸ', b'\xe2\xb4\xb8'], ['ꓦ', b'\xea\x93\xa6'], ['ꛟ', b'\xea\x9b\x9f'], ['𐔝', b'\xf0\x90\x94\x9d'], ['𑢠', b'\xf0\x91\xa2\xa0'], ['𖼈', b'\xf0\x96\xbc\x88'], ['𝈍', b'\xf0\x9d\x88\x8d'], ['𝐕', b'\xf0\x9d\x90\x95'], ['𝑉', b'\xf0\x9d\x91\x89'], ['𝑽', b'\xf0\x9d\x91\xbd'], ['𝒱', b'\xf0\x9d\x92\xb1'], ['𝓥', b'\xf0\x9d\x93\xa5'], ['𝔙', b'\xf0\x9d\x94\x99'], ['𝕍', b'\xf0\x9d\x95\x8d'], ['𝖁', b'\xf0\x9d\x96\x81'], ['𝖵', b'\xf0\x9d\x96\xb5'], ['𝗩', b'\xf0\x9d\x97\xa9'], ['𝘝', b'\xf0\x9d\x98\x9d'], ['𝙑', b'\xf0\x9d\x99\x91'], ['𝚅', b'\xf0\x9d\x9a\x85']],
    [ ['Ԝ', b'\xd4\x9c'], ['Ꮃ', b'\xe1\x8e\xb3'], ['Ꮤ', b'\xe1\x8f\x94'], ['ꓪ', b'\xea\x93\xaa'], ['𑣦', b'\xf0\x91\xa3\xa6'], ['𑣯', b'\xf0\x91\xa3\xaf'], ['𝐖', b'\xf0\x9d\x90\x96'], ['𝑊', b'\xf0\x9d\x91\x8a'], ['𝑾', b'\xf0\x9d\x91\xbe'], ['𝒲', b'\xf0\x9d\x92\xb2'], ['𝓦', b'\xf0\x9d\x93\xa6'], ['𝔚', b'\xf0\x9d\x94\x9a'], ['𝕎', b'\xf0\x9d\x95\x8e'], ['𝖂', b'\xf0\x9d\x96\x82'], ['𝖶', b'\xf0\x9d\x96\xb6'], ['𝗪', b'\xf0\x9d\x97\xaa'], ['𝘞', b'\xf0\x9d\x98\x9e'], ['𝙒', b'\xf0\x9d\x99\x92'], ['𝚆', b'\xf0\x9d\x9a\x86']],
    [ ['Χ', b'\xce\xa7'], ['Х', b'\xd0\xa5'], ['᙭', b'\xe1\x99\xad'], ['ᚷ', b'\xe1\x9a\xb7'], ['Ⅹ', b'\xe2\x85\xa9'], ['╳', b'\xe2\x95\xb3'], ['Ⲭ', b'\xe2\xb2\xac'], ['ⵝ', b'\xe2\xb5\x9d'], ['ꓫ', b'\xea\x93\xab'], ['Ꭓ', b'\xea\x9e\xb3'], ['𐊐', b'\xf0\x90\x8a\x90'], ['𐊴', b'\xf0\x90\x8a\xb4'], ['𐌗', b'\xf0\x90\x8c\x97'], ['𐌢', b'\xf0\x90\x8c\xa2'], ['𐔧', b'\xf0\x90\x94\xa7'], ['𑣬', b'\xf0\x91\xa3\xac'], ['𝐗', b'\xf0\x9d\x90\x97'], ['𝑋', b'\xf0\x9d\x91\x8b'], ['𝑿', b'\xf0\x9d\x91\xbf'], ['𝒳', b'\xf0\x9d\x92\xb3'], ['𝓧', b'\xf0\x9d\x93\xa7'], ['𝔛', b'\xf0\x9d\x94\x9b'], ['𝕏', b'\xf0\x9d\x95\x8f'], ['𝖃', b'\xf0\x9d\x96\x83'], ['𝖷', b'\xf0\x9d\x96\xb7'], ['𝗫', b'\xf0\x9d\x97\xab'], ['𝘟', b'\xf0\x9d\x98\x9f'], ['𝙓', b'\xf0\x9d\x99\x93'], ['𝚇', b'\xf0\x9d\x9a\x87'], ['𝚾', b'\xf0\x9d\x9a\xbe'], ['𝛸', b'\xf0\x9d\x9b\xb8'], ['𝜲', b'\xf0\x9d\x9c\xb2'], ['𝝬', b'\xf0\x9d\x9d\xac'], ['𝞦', b'\xf0\x9d\x9e\xa6'], ['Ｘ', b'\xef\xbc\xb8']],
    [ ['Υ', b'\xce\xa5'], ['ϒ', b'\xcf\x92'], ['У', b'\xd0\xa3'], ['Ү', b'\xd2\xae'], ['Ꭹ', b'\xe1\x8e\xa9'], ['Ꮍ', b'\xe1\x8e\xbd'], ['Ⲩ', b'\xe2\xb2\xa8'], ['ꓬ', b'\xea\x93\xac'], ['𐊲', b'\xf0\x90\x8a\xb2'], ['𑢤', b'\xf0\x91\xa2\xa4'], ['𖽃', b'\xf0\x96\xbd\x83'], ['𝐘', b'\xf0\x9d\x90\x98'], ['𝑌', b'\xf0\x9d\x91\x8c'], ['𝒀', b'\xf0\x9d\x92\x80'], ['𝒴', b'\xf0\x9d\x92\xb4'], ['𝓨', b'\xf0\x9d\x93\xa8'], ['𝔜', b'\xf0\x9d\x94\x9c'], ['𝕐', b'\xf0\x9d\x95\x90'], ['𝖄', b'\xf0\x9d\x96\x84'], ['𝖸', b'\xf0\x9d\x96\xb8'], ['𝗬', b'\xf0\x9d\x97\xac'], ['𝘠', b'\xf0\x9d\x98\xa0'], ['𝙔', b'\xf0\x9d\x99\x94'], ['𝚈', b'\xf0\x9d\x9a\x88'], ['𝚼', b'\xf0\x9d\x9a\xbc'], ['𝛶', b'\xf0\x9d\x9b\xb6'], ['𝜰', b'\xf0\x9d\x9c\xb0'], ['𝝪', b'\xf0\x9d\x9d\xaa'], ['𝞤', b'\xf0\x9d\x9e\xa4'], ['Ｙ', b'\xef\xbc\xb9']],
    [ ['Ζ', b'\xce\x96'], ['Ꮓ', b'\xe1\x8f\x83'], ['ℤ', b'\xe2\x84\xa4'], ['ℨ', b'\xe2\x84\xa8'], ['ꓜ', b'\xea\x93\x9c'], ['𐋵', b'\xf0\x90\x8b\xb5'], ['𑢩', b'\xf0\x91\xa2\xa9'], ['𑣥', b'\xf0\x91\xa3\xa5'], ['𝐙', b'\xf0\x9d\x90\x99'], ['𝑍', b'\xf0\x9d\x91\x8d'], ['𝒁', b'\xf0\x9d\x92\x81'], ['𝒵', b'\xf0\x9d\x92\xb5'], ['𝓩', b'\xf0\x9d\x93\xa9'], ['𝖅', b'\xf0\x9d\x96\x85'], ['𝖹', b'\xf0\x9d\x96\xb9'], ['𝗭', b'\xf0\x9d\x97\xad'], ['𝘡', b'\xf0\x9d\x98\xa1'], ['𝙕', b'\xf0\x9d\x99\x95'], ['𝚉', b'\xf0\x9d\x9a\x89'], ['𝚭', b'\xf0\x9d\x9a\xad'], ['𝛧', b'\xf0\x9d\x9b\xa7'], ['𝜡', b'\xf0\x9d\x9c\xa1'], ['𝝛', b'\xf0\x9d\x9d\x9b'], ['𝞕', b'\xf0\x9d\x9e\x95'], ['Ｚ', b'\xef\xbc\xba']],

    ]

    unicode_Position = 0

    count = 0
    for unicode_array in unicode_Letters:
        for tuple in unicode_array:
            if tuple[1] == findUtf:
                unicode_Position = count
        count = count + 1

    Latin_Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


    Value_to_return = Latin_Alphabets[unicode_Position]
    return Value_to_return


#Tested
# a = b'\xd0\xb5'
# print(unicode_Coversion(a))

