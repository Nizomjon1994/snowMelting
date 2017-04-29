/**
 * Created by nizom on 2/10/17.
 */
$("#countdown").countdown360({
radius      : 60,
seconds     : 100,
fontColor   : '#FFFFFF',
autostart   : false,
onComplete  : function () { console.log('done') }
}).start()
