class Store{
  constructor(storageApi){
    this.api = storageApi;
  }
  get(){
    return this.api.getItem(this.key);
  }
  set(val){
    this.api.setItem(this.key, val);
  }
}

export class UserStore extends Store{
  constructor(key){
    super(sessionStorage);
    this.key = key;
  }
}
