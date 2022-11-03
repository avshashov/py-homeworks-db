INSERT INTO performers (performer_name)
VALUES ('Yung Lean'),
       ('Bones'),
       ('Cannons'),
       ('Cream Soda'),
       ('Kate Bush'),
       ('Tame Impala'),
       ('Lurmish'),
       ('Wolf & Moon');


INSERT INTO genre (genre_name)
VALUES ('Hip-Hop'), ('Indie-Rock'), ('Indie-Pop'), ('Dance-Pop'), ('Rap');


INSERT INTO albums (album_name, release_date)
VALUES ('Starz', to_date('19 11 2020', 'DD MM YYYY')),
       ('DreamCard', to_date('13 09 2022', 'DD MM YYYY')),
       ('Night Drive', to_date('12 05 2017', 'DD MM YYYY')),
       ('Красиво', to_date('30 03 2018', 'DD MM YYYY')),
       ('Hounds of Love', to_date('16 09 1985', 'DD MM YYYY')),
       ('Currents', to_date('17 08 2015', 'DD MM YYYY')),
       ('Гипнос', to_date('26 11 2021', 'DD MM YYYY')),
       ('Суперблиц', to_date('25 05 2018', 'DD MM YYYY')),
       ('Follow the Signs', to_date('20 11 2020', 'DD MM YYYY'));


INSERT INTO tracks (track_name, album_id, duration)
VALUES ('Yayo', 1, '00:02:37'),
       ('Outta My Head', 1, '00:02:51'),
       ('Silverado', 2, '00:02:16'),
       ('GetAJob', 2, '00:01:39'),
       ('Miracle', 3, '00:04:27'),
       ('Can You Feel It', 3, '00:03:14'),
       ('Красиво', 4, '00:02:53'),
       ('Время против нас', 4, '00:04:25'),
       ('Running Up That Hill', 5, '00:05:01'),
       ('The Big Sky', 5, '00:04:35'),
       ('Let It Happen', 6, '00:07:47'),
       ('The Less I Know the Better', 6, '00:03:39'),
       ('Изобилие', 7, '00:03:33'),
       ('Маршрут', 7, '00:03:40'),
       ('Радар', 8, '00:03:46'),
       ('The Road', 9, '00:03:07'),
       ('Situations', 9, '00:03:05');


INSERT INTO music_collections (collection_name, release_date)
VALUES ('Сборник_1', to_date('19 03 2018', 'DD MM YYYY')),
       ('Сборник_2', to_date('29 11 2017', 'DD MM YYYY')),
       ('Сборник_3', to_date('14 07 2020', 'DD MM YYYY')),
       ('Сборник_4', to_date('15 06 2021', 'DD MM YYYY')),
       ('Сборник_5', to_date('12 10 2019', 'DD MM YYYY')),
       ('Сборник_6', to_date('18 12 2022', 'DD MM YYYY')),
       ('Сборник_7', to_date('14 11 2022', 'DD MM YYYY')),
       ('Сборник_8', to_date('13 01 2022', 'DD MM YYYY'));

INSERT INTO genre_performers (genre_id, performer_id)
VALUES (1, 1),
       (1, 2),
       (2, 6),
       (2, 8),
       (3, 3),
       (3, 6),
       (4, 4),
       (5, 1),
       (5, 2);


INSERT INTO album_performers (performer_id, album_id)
VALUES (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (7, 8),
        (8, 9);


INSERT INTO collection_tracks (collection_id, track_id)
VALUES (1, 1),
       (1, 2),
       (1, 3),
       (1, 4),
       (2, 5),
       (2, 1),
       (2, 3),
       (2, 4),
       (3, 12),
       (3, 11),
       (3, 7),
       (3, 4),
       (4, 4),
       (4, 9),
       (5, 15),
       (5, 16),
       (5, 1),
       (5, 9);



