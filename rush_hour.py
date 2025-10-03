# rush_hour.py

class Vehicle:
    def __init__(self, vid, x, y, orientation, length):
        """
        vid : str -> identifiant du véhicule (ex: 'A', 'B', 'X')
        x, y : int -> position du coin supérieur gauche du véhicule
        orientation : str -> 'H' ou 'V'
        length : int -> 2 (voiture) ou 3 (camion)
        """
        self.vid = vid
        self.x = x
        self.y = y
        self.orientation = orientation
        self.length = length

    def get_positions(self):
        """Retourne la liste des cases occupées par ce véhicule."""
        positions = []
        for i in range(self.length):
            if self.orientation == 'H':
                positions.append((self.x + i, self.y))
            else:
                positions.append((self.x, self.y + i))
        return positions


class RushHourPuzzle:
    def __init__(self):
        self.board_height = 0
        self.board_width = 0
        self.vehicles = []
        self.walls = []
        self.board = []

    def setVehicles(self, csv_file):
        """
        Lit le fichier CSV pour remplir :
        - self.board_height et self.board_width
        - self.vehicles (liste de Vehicle)
        - self.walls si nécessaire
        Format attendu dans le CSV :
        6,6              # dimensions du plateau
        X,0,2,H,2        # id, x, y, orientation, longueur
        A,1,0,H,2
        ...
        #,3,3            # mur éventuel (x,y)
        """
        with open(csv_file, "r") as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]

        # Dimensions
        self.board_height, self.board_width = map(int, lines[0].split(','))

        for line in lines[1:]:
            parts = line.split(',')
            if parts[0] == '#':  # mur
                x, y = int(parts[1]), int(parts[2])
                self.walls.append((x, y))
            else:
                vid, x, y, orientation, length = parts
                vehicle = Vehicle(vid, int(x), int(y), orientation, int(length))
                self.vehicles.append(vehicle)

    def setBoard(self):
        """Crée une matrice représentant le plateau."""
        self.board = [[" " for _ in range(self.board_width)] for _ in range(self.board_height)]

        # Placer les véhicules
        for v in self.vehicles:
            for (x, y) in v.get_positions():
                self.board[y][x] = v.vid

        # Placer les murs
        for (x, y) in self.walls:
            self.board[y][x] = "#"

    def isGoal(self):
        """
        Vérifie si la voiture rouge X est en position de sortie.
        Par convention, la sortie est à droite, donc X doit être
        dans la colonne (board_width - 2) sur la bonne ligne.
        """
        red_car = next(v for v in self.vehicles if v.vid == "X")
        # La position du coin gauche de X + longueur doit atteindre la dernière colonne - 1
        return red_car.x + red_car.length == self.board_width

    def successorFunction(self):
        """
        Génère les mouvements possibles.
        Retourne une liste de tuples : (action, nouvel_etat)
        action = (vid, direction)  ex: ('A', 'R') pour 'move right'
        """
        successors = []

        # Pour chaque véhicule, essayer de bouger d'une case dans les directions valides
        for v in self.vehicles:
            if v.orientation == 'H':
                # Vers la gauche
                if self.is_free(v.x - 1, v.y):
                    successors.append(((v.vid, 'L'), self.move_vehicle(v, -1, 0)))
                # Vers la droite
                if self.is_free(v.x + v.length, v.y):
                    successors.append(((v.vid, 'R'), self.move_vehicle(v, +1, 0)))
            else:  # orientation verticale
                # Vers le haut
                if self.is_free(v.x, v.y - 1):
                    successors.append(((v.vid, 'U'), self.move_vehicle(v, 0, -1)))
                # Vers le bas
                if self.is_free(v.x, v.y + v.length):
                    successors.append(((v.vid, 'D'), self.move_vehicle(v, 0, +1)))

        return successors

    def is_free(self, x, y):
        """Vérifie si la case (x,y) est libre et dans les bornes."""
        if x < 0 or x >= self.board_width or y < 0 or y >= self.board_height:
            return False
        return self.board[y][x] == " "

    def move_vehicle(self, vehicle, dx, dy):
        """
        Retourne un nouvel objet RushHourPuzzle où le véhicule a été déplacé.
        """
        new_state = RushHourPuzzle()
        new_state.board_height = self.board_height
        new_state.board_width = self.board_width
        new_state.walls = self.walls.copy()
        new_state.vehicles = []
        for v in self.vehicles:
            if v.vid == vehicle.vid:
                new_vehicle = Vehicle(v.vid, v.x + dx, v.y + dy, v.orientation, v.length)
            else:
                new_vehicle = Vehicle(v.vid, v.x, v.y, v.orientation, v.length)
            new_state.vehicles.append(new_vehicle)
        new_state.setBoard()
        return new_state

    def __str__(self):
        """Affichage du plateau sous forme de texte."""
        return "\n".join("".join(row) for row in self.board)
