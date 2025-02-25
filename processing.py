


def list_move_to_string(moves: list, env):
    for idx, move in enumerate(moves):
        moves[idx] = env.move_to_string(move)

    return moves


def clean_moves(moves):
    cleaned_moves = []
    for move in moves:
        # Gestion des coups particuliers
        if move in ["O-O", "O-O-O"]:
            cleaned_moves.append(move)
        else:
            # Gestion des coups normaux
            if len(move) <= 4:
                # Si le mouvement est simple (comme 'a2a3')
                cleaned_moves.append(move[-2:])
            elif "x" in move:

                cleaned_moves.append(move[0] + move[-3:])

            else:
                # Si le mouvement implique une pièce (comme 'Nb1a3')
                cleaned_moves.append(move[:-4] + move[-2:])
    return cleaned_moves

def find_most_similar_move_char_overlap(move_pgn, cleaned_moves):
    """
    Trouve l'index du coup le plus similaire dans cleaned_moves à move_pgn
    en se basant sur le nombre de caractères en commun.
    """
    best_similarity_score = 0
    best_match_index = None

    for i, cleaned_move in enumerate(cleaned_moves):
        similarity_score = 0
        for char_move_pgn in move_pgn:
            if char_move_pgn in cleaned_move:
                similarity_score += 1

        if similarity_score > best_similarity_score:
            best_similarity_score = similarity_score
            best_match_index = i

    return best_match_index
