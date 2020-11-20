# 撰寫一程式，程式檔名為 is_prime.py
# 提示使用者輸入一數字（100 以內的正整數），判斷此數字是否為質數，
# 若為質數，顯示 '是質數' ，反之顯示 '不是質數' 。
input(int(x))
factor = 2
while(factor<=x){
	isPrime = 1
	for(i=2;i<=pow(factor,0.5);i++){
		if(factor%i==0){
			isPrime = 0
			break
		}
			
	}
	    	
	if(isPrime == 0){
		factor++
		continue
			
	}
	  cout<<factor<<"^"<<a=x/factor;<<"\t"
}
cout<<endl 
return 0
} 