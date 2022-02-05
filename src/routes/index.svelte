<script>
	import { onMount } from 'svelte';
	let songs;
	let songImage;

	const getSongs = (songListData) => {
		const songList = songListData.filter((song) => song.resultType === 'song');
		return songList;
	};

	const getMaxImageSizeURL = (song) => {
		let imageLenght = song.thumbnails.slice(-1);
		return imageLenght[0].url;
	};

	onMount(async () => {
		const response = await fetch('http://127.0.0.1:5002/music/Three');
		// const response = await fetch('https://api.publicapis.org/entries');
		const data = await response.json();
		// topSongName = songs;
		songs = getSongs(data);
		console.log(songs);
	});
</script>

<section>
	<h1>Muse Player</h1>
	<h2>TopSong</h2>
	<input type="search" name="" id="" placeholder="Search Song" />
	{#if songs == undefined}
		Loading songs
	{:else}
		{#each songs as song}
			<h3>{song.title}</h3>
			<img src={getMaxImageSizeURL(song)} alt="" />
		{/each}
	{/if}
</section>

<style>
	section {
		display: grid;
		align-content: center;
		max-width: 500px;
	}
	h1 {
		font-size: 32px;
	}
	h2 {
		font-size: 28px;
	}
	h3 {
		font-size: 21px;
	}
	.song {
		background-color: black;
		color: blanchedalmond;
		padding: 3rem;
	}
	.song img {
		width: 100%;
	}
</style>
