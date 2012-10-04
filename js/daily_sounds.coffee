$ ->
  StartDate = new Date(2012, 9, 5)
  diff = parseInt((new Date().getTime() / 1000 - StartDate.getTime() / 1000) / (60 * 60 * 24))
  index_today = diff % 3
  day_str = ['miku', 'gumi', 'luka']
  singer_name =
    'miku': '初音ミク'
    'gumi': 'GUMI'
    'luka': '巡音ルカ'

  songs_name = [
    ["夕焼け小焼け", "ロンドン橋落ちた", "シャボン玉"]
    ["きらきら星", "どんぐりころころ","さくら"]
    ["あめふり", "ひなまつり", "荒城の月"]
  ]

  status = ['before', 'after']
  for i in [0..2]
    $vcl_editor = $('</p>').append("音源: VOCALOID&trade;2 #{singer_name[day_str[index_today]]}").prependTo(".service_demo:eq(#{i})")
    $song_name = $('</p>').append("曲名: #{songs_name[index_today][i]}").prependTo(".service_demo:eq(#{i})")
    for j in [0..1]
      $('source:even').eq(i * 2 + j).attr({src: "audio/#{day_str[index_today]}#{i}_#{status[j]}.ogg", type: "audio/ogg"})
      $('source:odd').eq(i * 2 + j).attr({src: "audio/#{day_str[index_today]}#{i}_#{status[j]}.mp3", type: "audio/mpeg"})
  return
