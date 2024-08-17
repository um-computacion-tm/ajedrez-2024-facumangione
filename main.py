from chess import Chess

def main():
    chess = Chess()    
    
def play(chess):        
    try:
        from_row = int(input("From row: "))
        from_rol = int(input("From row: "))
        to_row = int(input("From row: "))
        to_col = int(input("From row: "))    
        
        chess.move (
        from_row,
        from_rol,
        to_row,
        to_col,
    )
    
    except Exception as e:
        print("error")
    

if __name__ == '__main__':
    main()