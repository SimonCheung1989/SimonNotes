1. Node常用命令    
https://www.oschina.net/news/79226/10-tips-and-tricks-that-will-make-you-an-npm-ninja    

2. npm install xxx -g 时， 模块将被下载安装到【全局目录】中。    
【全局目录】通过 npm config set prefix "目录路径" 来设置。    
通过 npm config get prefix 来获取当前设置的目录。    

3. npm install xxx ，则是将模块下载到当前命令行所在目录    

4. package.json    
	dependencies:    
	devDependencies:    
	peerDependencies:    
	bundledDependencies:    
	optionalDependencies:    
	[reference](https://stackoverflow.com/questions/18875674/whats-the-difference-between-dependencies-devdependencies-and-peerdependencies)
