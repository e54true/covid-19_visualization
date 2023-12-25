void main(){
    fork();
    if(fork()==0){
        fork();
    }
    else if(fork()>0){
        fork();
    }
}