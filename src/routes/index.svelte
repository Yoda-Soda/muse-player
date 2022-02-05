<script>
	import { onMount } from 'svelte';
	let songs;
	let timer;
	let statusMsg = 'Try searching for songs';

	const debounce = (v) => {
		clearTimeout(timer);
		timer = setTimeout(async () => {
			if (v === '') {
				statusMsg = 'No songs searched';
				songs = undefined;
			} else {
				statusMsg = 'Searching Songs';
			}
			const response = await fetch('http://127.0.0.1:5002/music/' + v);
			const data = await response.json();
			songs = getSongs(data);
			console.log(songs);
		}, 1000);
	};

	const getSongs = (songListData) => {
		const songList = songListData.filter((song) => song.resultType === 'song');
		return songList;
	};

	const getMaxImageSizeURL = (song) => {
		let imageLenght = song.thumbnails.slice(-1);
		return imageLenght[0].url;
	};

	// onMount(async () => {
	// 	const response = await fetch('http://127.0.0.1:5002/music/Three');
	// 	const data = await response.json();
	// 	songs = getSongs(data);
	// });
</script>

<div class="main">
	<img
		class="logo-img"
		src="/kisspng-felix-the-cat-logo-cat-head-5accb146c37776.1067276615233641668006.png"
		alt=""
	/>
	<h1>Mewso Player</h1>
	<input
		type="search"
		name=""
		id=""
		placeholder="Search Song"
		on:keyup={({ target: { value } }) => debounce(value)}
	/>
	{#if songs == undefined}
		{statusMsg}
	{:else}
		<div class="songs">
			{#each songs as song}
				<section class="song">
					<img src={getMaxImageSizeURL(song)} alt={song.title} />
					<div class="content">
						<h3>{song.title}</h3>
						<p>by: {song.artists[0].name}</p>
						<p>length: {song.duration}</p>
					</div>
					<!-- <iframe
				width="200"
				height="200"
				src="https://www.youtube.com/embed/{song.videoId}"
				title="YouTube video player"
				frameborder="0"
				allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
				allowfullscreen
				/> -->
				</section>
			{/each}
		</div>
	{/if}
</div>

<style>
	.logo-img {
		width: 90px;
	}
	input {
		padding: 1rem;
		margin-bottom: 2rem;
		width: 93%;
		max-width: 600px;
	}
	.main {
		width: 90%;
		max-width: 1400px;
		margin: 0 auto;
		display: grid;
		justify-items: center;
	}
	h1 {
		font-size: 32px;
	}
	h3 {
		font-size: 21px;
	}
	.songs {
		display: grid;
		width: 100%;
		justify-content: center;
		grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		gap: 50px;
	}
	.song {
		box-shadow: 6px 10px 16px 4px rgba(0, 0, 0, 0.14);
		border-radius: 7px;
		background-color: black;
		color: white;
		font-weight: 700;
	}
	.content {
		padding: 0 2rem;
	}
	.song img {
		border-top-left-radius: 7px;
		border-top-right-radius: 7px;
		width: 100%;
	}
</style>
