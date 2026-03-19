class TestCreateMovie:
    """Tests for movie creation."""

    def test_create_movie_success(self, client, auth_header, sample_movie):
        response = client.post(
            "/api/v1/movies/",
            json=sample_movie,
            headers=auth_header
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == sample_movie["title"]
        assert data["director"] == sample_movie["director"]
        assert data["year"] == sample_movie["year"]
        assert data["genre"] == sample_movie["genre"]
        assert data["rating"] == sample_movie["rating"]
        assert "id" in data
        assert "created_at" in data

    def test_create_movie_without_auth(self, client, sample_movie):
        response = client.post("/api/v1/movies/", json=sample_movie)
        assert response.status_code == 401

    def test_create_movie_invalid_year(self, client, auth_header):
        response = client.post(
            "/api/v1/movies/",
            json={
                "title": "Bad Movie",
                "director": "Someone",
                "year": 1800,  # Too old
                "genre": "Drama"
            },
            headers=auth_header
        )
        assert response.status_code == 422

    def test_create_movie_invalid_rating(self, client, auth_header):
        response = client.post(
            "/api/v1/movies/",
            json={
                "title": "Bad Movie",
                "director": "Someone",
                "year": 2020,
                "genre": "Drama",
                "rating": 15.0  # Max is 10
            },
            headers=auth_header
        )
        assert response.status_code == 422

    def test_create_movie_missing_required_fields(self, client, auth_header):
        response = client.post(
            "/api/v1/movies/",
            json={"title": "Only Title"},
            headers=auth_header
        )
        assert response.status_code == 422


class TestGetMovies:
    """Tests for retrieving movies."""

    def test_get_movies_empty(self, client):
        response = client.get("/api/v1/movies/")
        assert response.status_code == 200
        assert response.json() == []

    def test_get_movies_with_data(self, client, auth_header, sample_movie):
        # Create a movie first
        client.post(
            "/api/v1/movies/",
            json=sample_movie,
            headers=auth_header
        )

        response = client.get("/api/v1/movies/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["title"] == sample_movie["title"]

    def test_get_movies_pagination(self, client, auth_header):
        # Create 5 movies
        for i in range(5):
            client.post(
                "/api/v1/movies/",
                json={
                    "title": f"Movie {i}",
                    "director": "Director",
                    "year": 2020,
                    "genre": "Action"
                },
                headers=auth_header
            )

        # Get first 2
        response = client.get("/api/v1/movies/?skip=0&limit=2")
        assert len(response.json()) == 2

        # Get next 2
        response = client.get("/api/v1/movies/?skip=2&limit=2")
        assert len(response.json()) == 2

    def test_get_movies_search(self, client, auth_header):
        client.post(
            "/api/v1/movies/",
            json={
                "title": "Inception",
                "director": "Christopher Nolan",
                "year": 2010,
                "genre": "Sci-Fi"
            },
            headers=auth_header
        )
        client.post(
            "/api/v1/movies/",
            json={
                "title": "The Dark Knight",
                "director": "Christopher Nolan",
                "year": 2008,
                "genre": "Action"
            },
            headers=auth_header
        )

        # Search by title
        response = client.get("/api/v1/movies/?search=Inception")
        assert len(response.json()) == 1

        # Search by director
        response = client.get("/api/v1/movies/?search=Nolan")
        assert len(response.json()) == 2

    def test_get_movies_filter_genre(self, client, auth_header):
        client.post(
            "/api/v1/movies/",
            json={
                "title": "Movie 1",
                "director": "Dir",
                "year": 2020,
                "genre": "Action"
            },
            headers=auth_header
        )
        client.post(
            "/api/v1/movies/",
            json={
                "title": "Movie 2",
                "director": "Dir",
                "year": 2020,
                "genre": "Comedy"
            },
            headers=auth_header
        )

        response = client.get("/api/v1/movies/?genre=Action")
        data = response.json()
        assert len(data) == 1
        assert data[0]["genre"] == "Action"

    def test_get_movies_no_auth_required(self, client):
        """Public endpoint — no token needed."""
        response = client.get("/api/v1/movies/")
        assert response.status_code == 200


class TestGetMovie:
    """Tests for retrieving a single movie."""

    def test_get_movie_success(self, client, auth_header, sample_movie):
        create_response = client.post(
            "/api/v1/movies/",
            json=sample_movie,
            headers=auth_header
        )
        movie_id = create_response.json()["id"]

        response = client.get(f"/api/v1/movies/{movie_id}")
        assert response.status_code == 200
        assert response.json()["title"] == sample_movie["title"]

    def test_get_movie_not_found(self, client):
        response = client.get("/api/v1/movies/999")
        assert response.status_code == 404


class TestUpdateMovie:
    """Tests for updating movies."""

    def test_update_movie_success(self, client, auth_header, sample_movie):
        create_response = client.post(
            "/api/v1/movies/",
            json=sample_movie,
            headers=auth_header
        )
        movie_id = create_response.json()["id"]

        response = client.put(
            f"/api/v1/movies/{movie_id}",
            json={"title": "Updated Title", "rating": 9.5},
            headers=auth_header
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["rating"] == 9.5
        assert data["director"] == sample_movie["director"]  # Unchanged

    def test_update_movie_not_found(self, client, auth_header):
        response = client.put(
            "/api/v1/movies/999",
            json={"title": "Nope"},
            headers=auth_header
        )
        assert response.status_code == 404

    def test_update_movie_without_auth(self, client, auth_header, sample_movie):
        create_response = client.post(
            "/api/v1/movies/",
            json=sample_movie,
            headers=auth_header
        )
        movie_id = create_response.json()["id"]

        response = client.put(
            f"/api/v1/movies/{movie_id}",
            json={"title": "Hacked"}
            # No auth header
        )
        assert response.status_code == 401


class TestDeleteMovie:
    """Tests for deleting movies."""

    def test_delete_movie_success(self, client, auth_header, sample_movie):
        create_response = client.post(
            "/api/v1/movies/",
            json=sample_movie,
            headers=auth_header
        )
        movie_id = create_response.json()["id"]

        response = client.delete(
            f"/api/v1/movies/{movie_id}",
            headers=auth_header
        )
        assert response.status_code == 204

        # Verify it's gone
        get_response = client.get(f"/api/v1/movies/{movie_id}")
        assert get_response.status_code == 404

    def test_delete_movie_not_found(self, client, auth_header):
        response = client.delete(
            "/api/v1/movies/999",
            headers=auth_header
        )
        assert response.status_code == 404

    def test_delete_movie_without_auth(self, client, auth_header, sample_movie):
        create_response = client.post(
            "/api/v1/movies/",
            json=sample_movie,
            headers=auth_header
        )
        movie_id = create_response.json()["id"]

        response = client.delete(f"/api/v1/movies/{movie_id}")
        assert response.status_code == 401
