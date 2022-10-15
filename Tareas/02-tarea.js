

class Queque{

    constructor( queue = [], len = 10 ){
        this.queue = queue
        this.len   = len
    }

    // Metodos comodin
    addWildcard( element ){
        return [ ...this.queue, element ]   
    }

    shiftWildCard( arr ){
        
       const arrHead = arr.shift()
        return arrHead
    }

    // Métodos basicos
    offer( element ){
        
        this.queue = this.addWildcard( element )
        return this.queue
    }

    poll(){
        if( this.queue.length > 0 ){
            this.shiftWildCard( this.queue )
            return true
        }
        return null
    }

    peek(){
        return this.queue[0]
    }

    size(){
        return this.queue.length + 1
    }

    // Métodos adicionales
    add( element ){

        if( this.queue.length <= this.len ){
            this.queue = this.addWildcard( element )

            return true
        }
        return false
    }

    remove(){
        return this.shiftWildCard( this.queue )
    }

    element(){
        return this.queue[0]
    }   
    // Seed

    createQueue(){
        
        for( let i = 0; i < this.len; i++ ){
            
            let newNumber = Math.round(Math.random() * 10)
            this.queue = this.addWildcard( newNumber )
        }

        console.log( 'Queue creado executa el metodo getQueue para verlo' ) 
        return
    }
}

