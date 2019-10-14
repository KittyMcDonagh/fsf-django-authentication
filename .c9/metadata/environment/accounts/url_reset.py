{"filter":false,"title":"url_reset.py","tooltip":"/accounts/url_reset.py","undoManager":{"mark":58,"position":58,"stack":[[{"start":{"row":11,"column":116},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":115},"action":"insert","lines":["url('^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),"],"id":40}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["r"],"id":42}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":116},"action":"remove","lines":["url(r'^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),"],"id":43},{"start":{"row":12,"column":4},"end":{"row":13,"column":4},"action":"remove","lines":["","    "]}],[{"start":{"row":13,"column":69},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":44},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":78},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":47},{"start":{"row":16,"column":78},"end":{"row":16,"column":79},"action":"remove","lines":[" "]},{"start":{"row":16,"column":78},"end":{"row":16,"column":79},"action":"remove","lines":[" "]},{"start":{"row":16,"column":78},"end":{"row":16,"column":79},"action":"remove","lines":[" "]},{"start":{"row":16,"column":78},"end":{"row":16,"column":79},"action":"remove","lines":[" "]}],[{"start":{"row":16,"column":177},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":49}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "],"id":50}],[{"start":{"row":17,"column":4},"end":{"row":18,"column":105},"action":"insert","lines":[" url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,","        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),"],"id":51}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":[" "],"id":52}],[{"start":{"row":17,"column":77},"end":{"row":18,"column":0},"action":"remove","lines":["",""],"id":53},{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":[" "]},{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":[" "]},{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":[" "]},{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":[" "]},{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":[" "]},{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":[" "]}],[{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":[" "],"id":54}],[{"start":{"row":16,"column":151},"end":{"row":16,"column":152},"action":"remove","lines":["\""],"id":55},{"start":{"row":16,"column":150},"end":{"row":16,"column":151},"action":"remove","lines":[" "]}],[{"start":{"row":16,"column":150},"end":{"row":16,"column":151},"action":"insert","lines":["'"],"id":56}],[{"start":{"row":16,"column":148},"end":{"row":16,"column":149},"action":"remove","lines":[" "],"id":57}],[{"start":{"row":16,"column":172},"end":{"row":16,"column":173},"action":"remove","lines":["\""],"id":58}],[{"start":{"row":16,"column":172},"end":{"row":16,"column":173},"action":"insert","lines":["'"],"id":59}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":175},"action":"remove","lines":["url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),"],"id":60}],[{"start":{"row":19,"column":83},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":80},"action":"insert","lines":["url(r'^complete/$', password_reset_complete, name='password_reset_complete')"],"id":62}],[{"start":{"row":19,"column":53},"end":{"row":19,"column":54},"action":"remove","lines":[" "],"id":63}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"remove","lines":[" "],"id":64},{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"remove","lines":["\""]}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":["'"],"id":65}],[{"start":{"row":19,"column":78},"end":{"row":19,"column":79},"action":"remove","lines":["\""],"id":66}],[{"start":{"row":19,"column":78},"end":{"row":19,"column":79},"action":"insert","lines":["'"],"id":67}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":80},"action":"remove","lines":["url(r'^complete/$', password_reset_complete, name='password_reset_complete')"],"id":68}],[{"start":{"row":19,"column":80},"end":{"row":19,"column":81},"action":"remove","lines":[","],"id":69}],[{"start":{"row":13,"column":69},"end":{"row":14,"column":4},"action":"remove","lines":["","    "],"id":70},{"start":{"row":13,"column":69},"end":{"row":14,"column":4},"action":"remove","lines":["","    "]}],[{"start":{"row":14,"column":78},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":71},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"insert","lines":["    "],"id":72}],[{"start":{"row":15,"column":74},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":73},{"start":{"row":16,"column":0},"end":{"row":16,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":16,"column":39},"end":{"row":17,"column":4},"action":"remove","lines":["","    "],"id":74}],[{"start":{"row":16,"column":39},"end":{"row":17,"column":8},"action":"remove","lines":["","        "],"id":75}],[{"start":{"row":17,"column":80},"end":{"row":18,"column":4},"action":"remove","lines":["","    "],"id":76},{"start":{"row":17,"column":80},"end":{"row":18,"column":4},"action":"remove","lines":["","    "]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":77}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":50},"action":"insert","lines":["from django.core.urlresolvers import reverse_lazy\""],"id":78}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["\""],"id":79}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":49},"action":"remove","lines":["from django.core.urlresolvers import reverse_lazy"],"id":80}],[{"start":{"row":4,"column":36},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":81}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":49},"action":"insert","lines":["from django.core.urlresolvers import reverse_lazy"],"id":82}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":49},"action":"remove","lines":["from django.core.urlresolvers import reverse_lazy"],"id":83}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["c"],"id":84},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["o"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["n"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["f"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["."]}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"remove","lines":["f"],"id":85},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"remove","lines":["n"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"remove","lines":["o"]},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"remove","lines":["c"]},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":["."]}],[{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"insert","lines":[" "],"id":86},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":["r"]},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"insert","lines":["e"]},{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":["v"]},{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":["e"]},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["r"]},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["e"],"id":87},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["_"]},{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":["l"]},{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"insert","lines":["a"]}],[{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":["z"],"id":88},{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"remove","lines":["t"],"id":89}],[{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"insert","lines":["y"],"id":90}],[{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"insert","lines":[","],"id":91}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"remove","lines":["y"],"id":92},{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"remove","lines":["z"]},{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"remove","lines":["a"]},{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"remove","lines":["l"]},{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"remove","lines":["_"]},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"remove","lines":["e"]},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"remove","lines":["s"]},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"remove","lines":["r"]},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"remove","lines":["e"]},{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"remove","lines":["v"]},{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"remove","lines":["e"]},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"remove","lines":["r"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"remove","lines":[" "]}],[{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"remove","lines":[","],"id":93}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":94}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":49},"action":"insert","lines":["from django.core.urlresolvers import reverse_lazy"],"id":95}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":49},"action":"remove","lines":["from django.core.urlresolvers import reverse_lazy"],"id":96},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":49},"action":"insert","lines":["from django.core.urlresolvers import reverse_lazy"],"id":97}],[{"start":{"row":8,"column":49},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":98}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":49},"action":"insert","lines":["from django.core.urlresolvers import reverse_lazy"],"id":99}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":49},"action":"remove","lines":["from django.core.urlresolvers import reverse_lazy","from django.core.urlresolvers import reverse_lazy"],"id":100},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":0},"end":{"row":8,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1570815329560,"hash":"f3f41b67925d40926c212dee3939755a58d01a35"}