/**
 * @license Copyright (c) 2003-2018, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    //富文本编辑器实现图片上传功能
    config.filebrowserImageUploadUrl = "/upload/";
    //代码高亮
    config.extraPlugins: "codesnippet";
    'extraPlugins': ','.join(['codesnippet','uploadimage','prism','widget','lineutils',]),
};
