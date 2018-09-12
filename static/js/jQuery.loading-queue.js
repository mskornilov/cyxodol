;(function ($) {

	var pluginName = 'loadingQueue';

	var LoadingQueue = function() {

		var self = this;

		this.queue = new Array();

		this.loading = false;

        this.sizes = [300, 500, 1000, 1500, 2000];

		this.buildUrl = function(image, options) {

			var url = null;

			if(options) {

				$.each(options, function(prefix, size) {

					if(!url || screen.width > size.width && screen.height > size.height) {
						url = image.data('basePath') + prefix + image.data('fileName');
					}
				});

			} else if(image.data('src')) {

				url = image.data('src');

			} else {

				url = image.data('basePath') + image.data('fileName');
			}

			return url;
		};

		this.dequeue = function () {

			var item = this.queue.shift();

			if(item) {

				this.loading = true;

				if(!item.image.is('img')) {
					this.dequeue();
					return;
				}

				var src = this.buildUrl(item.image, item.options);

                if (retina && ($('.galcategory').length || $('.photo.gallery').length)) {
                    var fileName = src;
                    var fullFileInfo = fileName.split('/');
                    var fileFullName = fullFileInfo.pop();
                    var basePath =  fullFileInfo.join('/');

                    var fileInfo = fileFullName.split('-');
                    var prefix = fileInfo[0];
                    fileInfo.shift()
                    var file = fileInfo.join('-');

                    if (parseInt(prefix) < 2000 && parseInt(prefix) >= 300) {
                        var index = self.sizes.indexOf((parseInt(prefix)));
                        prefix = self.sizes[index + 1];
                        src = basePath + '/' + prefix + '-' + file;
                    }
                }

				if(document.cookie.indexOf('_gphw_mode=mobile') >= 0 && ($('.galcategory').length || $('.photo.gallery').length)){

					var isVimeo = ~src.indexOf("vimeo");
					var isYouTube = ~src.indexOf("ytimg");

					if(!isVimeo && !isYouTube){
						var fileName = src;
						var fullFileInfo = fileName.split('/');
						var fileFullName = fullFileInfo.pop();
						var basePath =  fullFileInfo.join('/');

						var fileInfo = fileFullName.split('-');
						fileInfo.shift();
						var file = fileInfo.join('-');

						src = basePath + '/1000-' + file;
					}

				}

				item.image
					.on('load', function() {

						item.image.trigger('loaded');

						self.dequeue();
					})
					.on('error', function() {

						self.dequeue();
					})
					.attr('src', src);

			} else {
				this.loading = false;
			}
		};

		this.enqueue = function(image, options) {

			this.queue.push({
				image: $(image),
				options: options
			});
		};
	};

	$.fn[pluginName] = function (options) {

		var q = new LoadingQueue();

		$(this).each(function() {

			q.enqueue($(this), options);

			if(!q.loading) {
				q.dequeue();
			}

		});

		return this;
	};

})(jQuery);
